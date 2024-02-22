from Admin import *


class OperationsManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self):
        print("Program Options: ")
        messages = [
            '1) Add book',
            '2) Print library books',
            '3) print books by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users'
        ]
        print('\n'.join(messages))
        msg = f"Enter your choice from 1 to {len(messages)} \n"
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        choice = self.print_menu()
        while True:
            if choice == 1:  # add_book(self, book_id, book_name, book_quantity)
                book_id = input('Please Enter the book id: \n')
                book_name = input('Please Enter the book name: \n')
                book_quantity = input('Please Enter the book quantity \n')
                self.admin.add_book(book_id, book_name, book_quantity)
            elif choice == 2:
                print(self.admin.print_all_books())
            elif choice == 3:
                query = str(input('Enter your query: \n'))
                print(', '.join(self.admin.search_for_book(query)))
            elif choice == 4:
                user_id = int(input('Enter user id: \n'))
                user_name = str(input('Enter user name: \n'))
                self.admin.add_user(user_id, user_name)
            elif choice == 5:
                user_name = str(input('Enter user name: \n'))
                book_name = input('Enter book name: \n')
                self.admin.borrow_book(user_name, book_name)
            elif choice == 6:
                user_name = str(input('Enter user name: \n'))
                book_name = input('Enter book name: \n')
                self.admin.return_book(user_name, book_name)
            elif choice == 7:
                self.admin.print_users_borrowed()
            elif choice == 8:
                self.admin.print_all_users()
            else:
                break

            choice = self.print_menu()
