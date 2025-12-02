class Movies():

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):

    def __init__(self):
        super().__init__()  # Вызвал метод __init__() суперкласса

    def add_movie(self, movie):  # Переопределил метод
        super().add_movie(movie)
        print(f"Комедии: {self.movies}")


class Drama(Movies):

    def __init__(self):
        super().__init__()  # Вызвал метод __init__() суперкласса

    def add_movie(self, movie):  # Переопределил метод
        super().add_movie(movie)
        print(f"Драмы: {self.movies}")


comedy = Comedy()
drama = Drama()
comedy.add_movie('Большой куш')
drama.add_movie('Оружейный барон')