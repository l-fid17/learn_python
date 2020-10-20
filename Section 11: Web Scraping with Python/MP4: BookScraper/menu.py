from app import books

USER_CHOICES = """
Enter one of the following:

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to get the next available book on the catalogue
- 'q' to exit

"""

def print_best_books():
    # best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10] # multiple sorting with a limit of 10 items
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)

def print_next_book():
    print(next(books_generator))
    

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

def menu():
    user_input = input(USER_CHOICES)
    while user_input != "q":
        if user_input in user_choices.keys():
            user_choices[user_input]()
        else:
            print("Invalid input")
        user_input = input(USER_CHOICES)


menu()