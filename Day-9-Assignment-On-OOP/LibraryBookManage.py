class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n <= 0 or n > self.__copies:
            raise ValueError("Invalid checkout operation")
        self.__copies -= n

    def return_book(self, n):
        if n <= 0:
            raise ValueError("Invalid return operation")
        self.__copies += n


# Example
b1 = Book("97812345", "Python", "John", 10)

b1.checkout(3)
print("Available:", b1.available)

b1.return_book(2)
print("Available:", b1.available)