from Admin import *

class OperationsManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self):
        print("Program Options: ")
        options = [
            '1) Add book',
            '2) Print library books',
            '3) Print books by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users'
        ]
        print('\n'.join(options))
        return self.get_choice(len(options))

    def get_choice(self, num_options):
        msg = f"Enter your choice from 1 to {num_options} \n"
        return input_is_valid(msg, 1, num_options)

    def add_book(self):
        book_id = input('Please Enter the book id: \n')
        book_name = input('Please Enter the book name: \n')
        book_quantity = input('Please Enter the book quantity: \n')
        self.admin.add_book(book_id, book_name, book_quantity)

    def print_books(self):
        print(self.admin.print_all_books())

    def search_books(self):
        query = input('Enter your query: \n')
        print(', '.join(self.admin.search_for_book(query)))

    def add_user(self):
        user_id = int(input('Enter user id: \n'))
        user_name = input('Enter user name: \n')
        self.admin.add_user(user_id, user_name)

    def borrow_book(self):
        user_name = input('Enter user name: \n')
        book_name = input('Enter book name: \n')
        self.admin.borrow_book(user_name, book_name)

    def return_book(self):
        user_name = input('Enter user name: \n')
        book_name = input('Enter book name: \n')
        self.admin.return_book(user_name, book_name)

    def print_users_borrowed(self):
        self.admin.print_users_borrowed()

    def print_all_users(self):
        self.admin.print_all_users()

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.search_books()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed()
            elif choice == 8:
                self.print_all_users()
            else:
                print("Exiting the program.")
                break
