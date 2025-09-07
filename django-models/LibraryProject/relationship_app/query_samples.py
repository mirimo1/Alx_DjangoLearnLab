from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian = library.librarian
print(librarian.name)