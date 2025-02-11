import asyncio
import collections
import random
import string
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Lock, Thread


class NoNewData(Exception):
    pass


def readline(handle):
    offset = handle.tell()
    handle.seek(0, 2)
    length = handle.tell()

    if length == offset:
        raise NoNewData
    # 移动光标，准备读取新行
    handle.seek(offset, 0)
    return handle.readline()


async def tail_async(handle, interval, write_func):
    loop = asyncio.get_event_loop()

    while not handle.closed:
        try:
            line = await loop.run_in_executor(None, readline, handle)
        except NoNewData:
            await asyncio.sleep(interval)
        else:
            await write_func(line)


def tail_file(handle, interval, write_func):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def write_rsync(data):
        await loop.run_in_executor(None, write_func, data)

    coro = tail_async(handle, interval, write_rsync)
    loop.run_until_complete(coro)


def run_threads(handles, interval, output_path):
    with open(output_path, "wb") as output:
        lock = Lock()

        def write(data):
            with lock:
                output.write(data)

        threads = []
        for handle in handles:
            args = handle, interval, write
            thread = Thread(target=tail_file, args=args)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()


# 写入随机数据
def write_random_data(path, write_count, interval):
    with open(path, "wb") as f:
        for i in range(write_count):
            time.sleep(random.random() * interval)
            letters = random.choices(string.ascii_lowercase, k=10)
            data = f'{path} - {i: 02} - {"".join(letters)}\n'
            f.write(data.encode("utf-8"))
            f.flush()


# 向多个文件写入随机数据
def start_write_threads(directory, file_count):
    paths = []
    for i in range(file_count):
        path = Path(directory) / str(i)
        with open(path, "w"):
            pass
        paths.append(path)
        args = path, 10, 0.1
        thread = Thread(target=write_random_data, args=args)
        thread.start()
    return paths


def close_all(handles):
    time.sleep(1)
    for handle in handles:
        handle.close()


def setup():
    tmpdir = TemporaryDirectory(dir="/")
    # print(tmpdir)
    input_paths = start_write_threads(tmpdir.name, 5)

    handles = []
    for path in input_paths:
        handle = open(path, "rb")
        handles.append(handle)

    Thread(target=close_all, args=(handles,)).start()

    output_path = Path(tmpdir.name) / "merged"
    return tmpdir, input_paths, handles, output_path


def confirm_merge(input_paths, output_path):
    found = collections.defaultdict(list)
    with open(output_path, "rb") as f:
        for line in f:
            for path in input_paths:
                if line.find(str(path).encode()) == 0:
                    found[path].append(line)

    expected = collections.defaultdict(list)
    for path in input_paths:
        with open(path, "rb") as f:
            expected[path].extend(f.readlines())

    for key, expected_lines in expected.items():
        found_lines = found[key]
        assert expected_lines == found_lines, f"{expected_lines!r} == {found_lines!r}"


tmpdir, input_paths, handles, output_path = setup()

# 合并文件
run_threads(handles, 0.1, output_path)

confirm_merge(input_paths, output_path)

tmpdir.cleanup()
