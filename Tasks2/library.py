class Library:
    books = [("ISBN1", "title1"), ("ISBN2", "title2")]

    def __init__(self, isbn: str, title: str):
        self.books.append((isbn, title))

    def find_book(self, isbn: str) -> str:
        for book, title in self.books:
            if isbn == book:
                return title
        return "None"


library = Library("DK194NF91", "NiceBook")
print(library.find_book("ISBN3"))