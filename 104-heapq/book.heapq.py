import functools
from heapq import heapify, heappop, heappush


@functools.total_ordering
class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.returned = False

    def __lt__(self, other):
        return self.due_date < other.due_date


def add_book(queue, book):
    heappush(queue, book)


queue = [
    Book("Pride and Prejudice", "2019-06-01"),
    Book("The Time Machine", "2019-05-30"),
    Book("Crime and Punishment", "2019-06-06"),
    Book("Wuthering Heights", "2019-06-12"),
]
heapify(queue)
print(
    [i.due_date for i in queue]
)  # ['2019-05-30', '2019-06-01', '2019-06-06', '2019-06-12']


class NoOverdueBooks(Exception):
    pass


def next_overdue_book(queue, now):
    while queue:
        book = queue[0]
        if book.returned:
            heappop(queue)
            continue

        if book.due_date < now:
            heappop(queue)
            return book
        break
    raise NoOverdueBooks


now = "2019-06-02"

book = next_overdue_book(queue, now)
print(book.due_date, book.title)

book = next_overdue_book(queue, now)
print(book.due_date, book.title)
