import json
import logging
from pathlib import Path

CUR_DIR = Path.cwd()
DATA_FILE = CUR_DIR / "data" / "movies.json"


def get_movies():

    with open(DATA_FILE, "r") as fichier:
        movies_title = json.load(fichier)
    movies = [Movie(movies_title) for movies_title in movies_title]
    return movies


class Movie:
    def __init__(self, title: str):
        self.m_movie = title.title()

    def __str__(self):
        return f"{self.m_movie}"

    @staticmethod
    def _get_movies():
        with open(DATA_FILE, "r") as fichier:
            return json.load(fichier)

    @staticmethod
    def _write_movies(movies):

        with open(DATA_FILE, "w") as fichier:
            json.dump(movies, fichier, indent=4)

    def add_to_movies(self):
        listes_de_films = self._get_movies()
        if self.m_movie in listes_de_films:
            logging.warning(f"Le film {self.m_movie} est deja dans la liste de films")
            return False
        else:
            listes_de_films.append(self.m_movie)
            self._write_movies(listes_de_films)
            return True

    def remove_from_movies(self):
        listes_de_fims = self._get_movies()
        if self.m_movie in listes_de_fims:
            listes_de_fims.remove(self.m_movie)
            self._write_movies(listes_de_fims)


if __name__ == "__main__":
    a = Movie("indiana jones")
    b = get_movies()
    for movie in b:
        print(movie.m_movie)

