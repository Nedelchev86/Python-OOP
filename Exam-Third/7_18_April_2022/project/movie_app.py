from project.movie_specification.movie import Movie
from project.user import User


class  MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if username in [u.username for u in self.users_collection]:
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = [u for u in self.users_collection if u.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for k, v in kwargs.items():
            if k == "title":
                movie.title = v
            elif k == "year":
                movie.year = v
            elif k == "age_restriction":
                movie.age_restriction = v
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if self.movies_collection:
            result = []
            [result.append(m.details()) for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]
            return "\n".join(result)
        else:
            return "No movies found."

    def __str__(self):
        result = []

        if self.users_collection:
            result.append(f"All users: {', '.join(u.username for u in self.users_collection)}")
        else:
            result.append("All users: No users.")

        if self.movies_collection:
            result.append(f"All movies: {', '.join(m.title for m in self.movies_collection)}")
        else:
            result.append("All movies: No movies.")
        return "\n".join(result)