import asyncio
import collections
import random
import string
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread


class NoNewData(Exception):
    pass


class WriteThread(Thread):
    def __init__(self, output_path):
        super().__init__()
        self.output_path = output_path
        self.output = None
        self.loop = asyncio.new_event_loop()

    def run(self):
        asyncio.set_event_loop(self.loop)
        with open(self.output_path, "wb") as self.output:
            self.loop.run_forever()

        self.loop.run_until_complete(asyncio.sleep(0))

    async def real_write(self, data):
        self.output.write(data)

    async def write(self, data):
        coro = self.real_write(data)
        future = asyncio.run_coroutine_threadsafe(coro, self.loop)
        await asyncio.wrap_future(future)

    async def real_stop(self):
        self.loop.stop()

    async def stop(self):
        coro = self.real_stop()
        future = asyncio.run_coroutine_threadsafe(coro, self.loop)
        await asyncio.wrap_future(future)

    async def __aenter__(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.start)
        return self

    async def __aexit__(self, *_):
        await self.stop()


def readline(handle):
    offset = handle.tell()
    handle.seek(0, 2)
    length = handle.tell()

    if length == offset:
        raise NoNewData

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


async def run_fully_async(handles, interval, output_path):
    async with WriteThread(output_path) as output, asyncio.TaskGroup() as group:
        for handle in handles:
            group.create_task(tail_async(handle, interval, output.write))


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
asyncio.run(run_fully_async(handles, 0.1, output_path))

confirm_merge(input_paths, output_path)

tmpdir.cleanup()
