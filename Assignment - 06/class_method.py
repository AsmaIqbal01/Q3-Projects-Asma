class Book:
    total_books=0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self,title):
        self.title = title
        Book.increment_book_count()

if __name__=="__main__":
    b1=Book("1984")
    print(Book.total_books)

    b2=Book("Brave New World")
    print(Book.total_books)

    b3=Book("Malice")
    print(Book.total_books)