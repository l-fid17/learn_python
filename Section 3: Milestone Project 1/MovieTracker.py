# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def get_data():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    return {"title": title, "director": director, "year": year}


def add_movie(user_data):
    movies.append(user_data)


# Create other functions for:

#   - listing movies
def list_movies():
    if len(movies) > 0:
        for movie in movies:
            print(movie)
    else:
        print("No movies in the list, yet.")


#   - finding movies
def find_movie(movie_to_find):
    for movie in movies:
        if movie["title"] == movie_to_find:
            print(movie)
        else:
            print("Could not find the movie.")


# And another function here for the user menu
def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            user_data = get_data()
            add_movie(user_data)
        elif selection == "l":
            list_movies()
        elif selection == "f":
            to_be_found = input("Enter the name of the movie to find: ")
            find_movie(to_be_found)
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!

user_menu()
