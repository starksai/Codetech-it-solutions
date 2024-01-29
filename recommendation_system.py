# Sample movie data (Movie, Genre)
movies = [
    {"title": "Movie A", "genre": "Action, Adventure"},
    {"title": "Movie B", "genre": "Drama, Romance"},
    {"title": "Movie C", "genre": "Action, Sci-Fi"},
    {"title": "Movie D", "genre": "Comedy"},
    {"title": "Movie E", "genre": "Drama, Mystery"},
    {"title": "Movie F", "genre": "Action, Thriller"},
    {"title": "Movie G", "genre": "Comedy, Romance"},
    {"title": "Movie H", "genre": "Sci-Fi, Adventure"},
    {"title": "Movie I", "genre": "Horror, Mystery"},
    {"title": "Movie J", "genre": "Action, Comedy"},
    {"title": "Movie K", "genre": "Drama, Fantasy"},
    {"title": "Movie L", "genre": "Romance, Comedy"},
    {"title": "Movie M", "genre": "Adventure, Family"},
    {"title": "Movie N", "genre": "Horror, Thriller"},
    {"title": "Movie O", "genre": "Animation, Family"},
]

def recommend_movie_based_on_genre(preferred_genre, movie_data):
    # Filter movies based on the preferred genre
    recommended_movies = [movie['title'] for movie in movie_data if preferred_genre.lower() in movie['genre'].lower()]

    if recommended_movies:
        return recommended_movies
    else:
        return "No movies found for the preferred genre."

# Get user input for preferred genre
user_genre_preference = input("Enter your preferred genre: ")

# Get recommendations based on user's preferred genre
recommendations = recommend_movie_based_on_genre(user_genre_preference, movies)

# Display recommendations
if isinstance(recommendations, list):
    print(f"Recommendations for {user_genre_preference}:")
    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")
else:
    print(recommendations)
