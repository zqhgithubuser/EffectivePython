import asyncio
import contextlib
import math
import random

WARMER = "Warmer"
COLDER = "Colder"
SAME = "Same"
UNSURE = "Unsure"
CORRECT = "Correct"


class EOFError(Exception):
    pass


class UnknownCommandError(Exception):
    pass


class AsyncConnection:
    def __init__(self, reader, writer):  # Changed
        self.reader = reader  # Changed
        self.writer = writer  # Changed

    async def send(self, command):
        line = command + "\n"
        data = line.encode()
        self.writer.write(data)  # Changed
        await self.writer.drain()  # Changed

    async def receive(self):
        line = await self.reader.readline()  # Changed
        if not line:
            raise EOFError("Connection closed")
        return line[:-1].decode()


class AsyncServerSession(AsyncConnection):  # Changed
    def __init__(self, *args):
        super().__init__(*args)
        self.clear_state()

    async def loop(self):  # Changed
        while command := await self.receive():  # Changed
            match command.split(" "):
                case "PARAMS", lower, upper:
                    self.set_params(lower, upper)
                case ["NUMBER"]:
                    await self.send_number()  # Changed
                case "REPORT", decision:
                    self.receive_report(decision)
                case ["CLEAR"]:
                    self.clear_state()
                case _:
                    raise UnknownCommandError(command)

    def set_params(self, lower, upper):
        self.clear_state()
        self.lower = int(lower)
        self.upper = int(upper)

    # 服务端猜数字
    def next_guess(self):
        if self.secret is not None:
            return self.secret

        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess

    async def send_number(self):  # Changed
        guess = self.next_guess()
        self.guesses.append(guess)
        await self.send(format(guess))  # Changed

    # 接收客户端的报告（decision）并打印
    def receive_report(self, decision):
        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last
        print(f"Server: {last} is {decision}")

    def clear_state(self):
        self.lower = None
        self.upper = None
        self.secret = None
        self.guesses = []


class AsyncClientSession:  # Changed
    def __init__(self, send, receive, secret):
        self.send = send
        self.receive = receive
        self.secret = secret
        self.last_distance = None

    # 接收服务器猜测的数字
    async def request_number(self):
        await self.send("NUMBER")  # Changed
        data = await self.receive()  # Changed
        return int(data)

    # 将结果（decision）报告给服务器
    async def report_outcome(self, number):  # Changed
        new_distance = math.fabs(number - self.secret)

        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            decision = UNSURE
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER
        else:
            decision = SAME

        self.last_distance = new_distance

        await self.send(f"REPORT {decision}")  # Changed
        return decision

    async def __aiter__(self):  # Changed
        while True:
            number = await self.request_number()  # Changed
            decision = await self.report_outcome(number)  # Changed
            yield number, decision
            if decision == CORRECT:
                return


@contextlib.asynccontextmanager  # Changed
async def new_async_game(connection, lower, upper, secret):  # Changed
    print(f"Guess a number between {lower} and {upper}! Shhhhh, it's {secret}.")

    await connection.send(f"PARAMS {lower} {upper}")  # Changed
    try:
        yield AsyncClientSession(
            connection.send,
            connection.receive,
            secret,
        )
    finally:
        await connection.send("CLEAR")  # Changed


async def handle_async_connection(reader, writer):  # Changed
    session = AsyncServerSession(reader, writer)  # Changed
    try:
        await session.loop()  # Changed
    except EOFError:
        pass


async def run_async_server(address):  # New
    server = await asyncio.start_server(handle_async_connection, *address)
    async with server:
        await server.serve_forever()


async def run_async_client(address):
    streams = await asyncio.open_connection(*address)  # New
    client = AsyncConnection(*streams)                 # New

    async with new_async_game(client, 1, 5, 3) as session:
        results = [outcome async for outcome in session]

    async with new_async_game(client, 10, 15, 12) as session:
        async for outcome in session:
            results.append(outcome)

    async with new_async_game(client, 1, 3, 2) as session:
        it = aiter(session)
        while True:
            try:
                outcome = await anext(it)
            except StopAsyncIteration:
                break
            else:
                results.append(outcome)

    _, writer = streams  # New
    writer.close()  # New
    await writer.wait_closed()  # New

    return results


async def main_async():
    address = ("127.0.0.1", 4321)
    server = run_async_server(address)
    asyncio.create_task(server)

    results = await run_async_client(address)
    for number, outcome in results:
        print(f"Client: {number} is {outcome}")


asyncio.run(main_async())
