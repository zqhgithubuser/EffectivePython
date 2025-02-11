class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date


def add_book(queue, book):
    queue.append(book)
    queue.sort(key=lambda x: x.due_date, reverse=True)


queue = []
add_book(queue, Book("Don Quixote", "2019-06-07"))
add_book(queue, Book("Frankenstein", "2019-06-05"))
add_book(queue, Book("Les Misérables", "2019-06-08"))
add_book(queue, Book("War and Peace", "2019-06-03"))


class NoOverdueBooks(Exception):
    pass


def next_overdue_book(queue, now):
    if queue:
        book = queue[-1]
        if book.due_date < now:
            queue.pop()
            return book

    raise NoOverdueBooks


now = "2019-06-10"

found = next_overdue_book(queue, now)
print(found.due_date, found.title)

found = next_overdue_book(queue, now)
print(found.due_date, found.title)


def return_book(queue, book):
    queue.remove(book)


queue = []
book = Book("Treasure Island", "2019-06-04")

add_book(queue, book)
print("Before return:", [x.title for x in queue])

return_book(queue, book)
print("After return: ", [x.title for x in queue])
