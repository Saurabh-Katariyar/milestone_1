# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

# Create other functions for:
#   - listing movies
#   - finding movies


def listing_movies():
    movie_list = []
    for movie in movies:
        movie_list.append(movie['title'])
    print(movie_list)


def find_movies():
    movie_name = input("Enter the movie name you want to find: ")
    movie_list = [x['title'] for x in movies]
    movie_list_lower = [x.lower() for x in movie_list]
    if movie_name.lower() in movie_list_lower:
        print('YES!')
    else:
        print('NO!')


user_selection = {
    'a': add_movie,
    'l': listing_movies,
    'f': find_movies
}

# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_selection:
            func = user_selection[selection]
            func()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()


# Remember to run the user menu function at the end!

