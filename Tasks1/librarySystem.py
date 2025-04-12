class Book:
    def __init__(self, title, author, release_year):
        self.title = title
        self.author = author
        self.release_year = release_year

    def description(self):
        return f"Book {self.title} by {self.author} released in {self.release_year}."

class Ebook(Book):
    def __init__(self, title, author, release_year, file_size):
        super().__init__(title, author, release_year)
        self.file_size = file_size

    def description(self):
        return f"Ebook {self.title} by {self.author} released in {self.release_year}, size {self.file_size} MB."

class Audiobook(Book):
    def __init__(self, title, author, release_year, duration):
        super().__init__(title, author, release_year)
        self.duration = duration

    def description(self):
        return f"Audiobook {self.title} by {self.author} released in {self.release_year}, lasts {self.duration} min."

eb1 = Ebook("Ebook1", "Author3", 1568, 52)
eb2 = Ebook("Ebook2", "Author4", 901, 125)
ab1 = Audiobook("Audiobook1", "Author1", 1337, 180)
ab2 = Audiobook("Audiobook2", "Author2", 1723, 360)

print(eb1.description())
print(eb2.description())
print(ab1.description())
print(ab2.description())