import contextlib
import math
import random
import socket
from threading import Thread

WARMER = "Warmer"
COLDER = "Colder"
SAME = "Same"
UNSURE = "Unsure"
CORRECT = "Correct"


class EOFError(Exception):
    pass


class UnknownCommandError(Exception):
    pass


class Connection:
    def __init__(self, connection):
        self.connection = connection
        self.file = connection.makefile("rb")

    def send(self, command):
        line = command + "\n"
        data = line.encode()
        self.connection.send(data)

    def receive(self):
        line = self.file.readline()
        if not line:
            raise EOFError("Connection closed")
        return line[:-1].decode()


class ServerSession(Connection):
    def __init__(self, *args):
        super().__init__(*args)
        self.clear_state()

    def loop(self):
        while command := self.receive():
            match command.split(" "):
                case "PARAMS", lower, upper:
                    self.set_params(lower, upper)
                case ["NUMBER"]:
                    self.send_number()
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

    def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        self.send(format(guess))

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


class ClientSession:
    def __init__(self, send, receive, secret):
        self.send = send
        self.receive = receive
        self.secret = secret
        self.last_distance = None

    # 接收服务器猜测的数字
    def request_number(self):
        self.send("NUMBER")
        data = self.receive()
        return int(data)

    # 将结果（decision）报告给服务器
    def report_outcome(self, number):
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

        self.send(f"REPORT {decision}")
        return decision

    def __iter__(self):
        while True:
            number = self.request_number()
            decision = self.report_outcome(number)
            yield number, decision
            if decision == CORRECT:
                return


@contextlib.contextmanager
def new_game(connection, lower, upper, secret):
    print(f"Guess a number between {lower} and {upper}! Shhhhh, it's {secret}.")

    connection.send(f"PARAMS {lower} {upper}")
    try:
        yield ClientSession(
            connection.send,
            connection.receive,
            secret,
        )
    finally:
        connection.send("CLEAR")


def handle_connection(connection):
    with connection:
        session = ServerSession(connection)
        try:
            session.loop()
        except EOFError:
            pass


def run_server(address):
    # server 线程
    with socket.socket() as listener:
        listener.bind(address)
        listener.listen()
        while True:
            connection, _ = listener.accept()
            thread = Thread(target=handle_connection, args=(connection,), daemon=True)
            thread.start()


def run_client(address):
    with socket.create_connection(address) as server_sock:
        server = Connection(server_sock)

        with new_game(server, 1, 5, 3) as session:
            results = [outcome for outcome in session]

        with new_game(server, 10, 15, 12) as session:
            for outcome in session:
                results.append(outcome)

        with new_game(server, 1, 3, 2) as session:
            it = iter(session)
            while True:
                try:
                    outcome = next(it)
                except StopIteration:
                    break
                else:
                    results.append(outcome)

    return results


def main():
    address = ("127.0.0.1", 1234)
    server_thread = Thread(target=run_server, args=(address,), daemon=True)
    server_thread.start()

    results = run_client(address)
    for number, outcome in results:
        print(f"Client: {number} is {outcome}")


main()
