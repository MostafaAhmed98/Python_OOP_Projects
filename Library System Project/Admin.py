from Book import *
from User import *
from utility import *


class Admin:
    def __init__(self):
        self.books = []  # book object
        self.users = {}  # user object as a key

    def add_book(self, book_id, book_name, book_quantity):
        for book in self.books:
            if book.id == book_id:
                return print("This book is already exist")
        new_book = Book(book_id, book_name, book_quantity)
        self.books.append(new_book)
        print("Book is added successfully")

    def print_all_books(self):
        lst_of_books = []
        for book in self.books:
            lst_of_books.append(book.name)
        if not lst_of_books:
            return f"There are no books"
        return ", ".join(lst_of_books)

    def search_for_book(self, query):
        found_books = [book.name for book in self.books if book.name[:len(query)].upper() == query.upper()]
        if not found_books:
            return f"No book found"
        return found_books

    def add_user(self, user_id, user_name):
        for user in self.users:
            if user.id == user_id:
                return print(f"This user already exist !")
        new_user = User(user_id, user_name)
        self.users[new_user] = None
        print("User created successfully !")

    def borrow_book(self, user_name, book_name):
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        available_books = [book for book in self.books if book.name == found_book and book.quantity > 0]
        if not available_books:
            return print("Insufficient quantity!")
        available_books[0].quantity -= 1
        for user, values in self.users.items():
            if user.name.lower() == user_name.lower():
                if values is None:
                    self.users[user] = [book_name]
                else:
                    self.users[user].append(book_name)
                user_found = True
        if not user_found:
            return print('There is no user with this name')
        return print(F'The user {user_name} borrowed {found_book}')

    def return_book(self, user_name, book_name):
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        available_books = [book for book in self.books if book.name == found_book]
        if not available_books:
            return print("There is no book with this name")
        available_books[0].quantity += 1
        for user, values in self.users.items():
            if user.name.lower() == user_name.lower():
                if len(values) == 1:
                    self.users[user] = None
                else:
                    self.users[user].remove(book_name)
                user_found = True
        if not user_found:
            return print('There is no user with this name')
        return print(F'The user {user_name} returned {found_book}')

    def print_users_borrowed(self):
        users_found = [user for user in self.users if self.users[user] is not None]
        if users_found:
            for user in users_found:
                print(f'The user {user.name} borrowed the books {" and ".join(self.users[user])}')
        else:
            print('There are no users borrowed any book')

    def print_all_users(self):
        all_users = [user.name for user in self.users]
        if all_users:
            for user in all_users:
                print(user, end=' ')
