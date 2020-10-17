from utils import databases

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input == 'l':
            list_all()
        elif user_input == 'r':
            mark_as_read()
        elif user_input == 'd':
            delete_book()
        else:
            print("Invalid input")
            
        user_input = input(USER_CHOICE)



def add_book():
    name_input = input("Name: ")
    author_input = input("Author: ")
    databases.add_book(name_input, author_input)

def list_all():
    databases.list_all_books()

def mark_as_read():
    databases.mark_as_read(input("Name: "))


def delete_book():
    databases.delete_book(input("Name: "))

    
menu()