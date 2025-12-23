# 1. Library Management System

# Design a program to manage a library that allows the user to:

# a) Issue a book

# b) Return a book

# c) Check list of books

# d) Calculate fine if the book is returned after 15 days

# e) View available books


books = ["C", "C++", "Python", "Java"]
issued = {}

def issue_book(name, book):
    if book in books:
        books.remove(book)
        issued[name] = book
        print(book,"issued to ", name)
    else:
        print("Book not available")

def return_book(name, days):
    book = issued.pop(name)
    books.append(book)
    if days > 15:
        print("Fine:", (days - 15) * 5)
    else:
        print("No fine")

issue_book("Aman", "Python")
return_book("Aman", 18)
print("Available books:", books)
