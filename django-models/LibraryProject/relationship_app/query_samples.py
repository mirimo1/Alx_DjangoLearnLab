from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
george = Author.objects.get(name="George Orwell")
books_by_george = Book.objects.filter(author=george)

# List all books in a library
central_library = Library.objects.get(name="Central Library")
books_in_library = central_library.books.all()

# Retrieve the librarian for a library
librarian = central_library.librarian