from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."


    def upload_movie(self, username: str, movie: Movie):
        try:
            c_user = [u for u in self.users_collection if u.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        
        if c_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        c_user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."



    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = [u for u in self.users_collection if u.username == username][0]
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = [u for u in self.users_collection if u.username == username][0]
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."


    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movies_liked.append(movie)
        movie.likes +=1
        return f"{username} liked {movie.title} movie."


    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."
        result = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        test = [x.details() for x in result]
        return "\n".join(test)

    def __str__(self):
        result = []
        if not self.users_collection:
            result.append("All users: No users.")
        else:
            result.append(f"All users: {', '.join([u.username for u in self.users_collection])}")

        if not self.movies_collection:
            result.append("All movies: No movies.")
        else:
            result.append(f"All movies: {', '.join([m.title for m in self.movies_collection])}")
        return "\n".join(result)
