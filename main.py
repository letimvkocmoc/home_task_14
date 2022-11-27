from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_by_title(title):
    """Поиск фильмов по названию"""

    content = get_by_title(title)

    return content


@app.route('/movie/<year_1>/to/<year_2>')
def movie_by_year(year_1, year_2):
    """Поиск фильмов по диапазону годов выпуска"""

    content = get_by_year(year_1, year_2)

    return content


@app.route('/rating/<category>')
def movie_by_rating(category):
    """Поиск фильмов возрастным категориям"""

    if category == 'children':
        content = get_children()
    elif category == 'family':
        content = get_family()
    elif category == 'adult':
        content = get_adult()

    return content


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    """Поиск фильмов по жанру"""

    content = get_by_genre(genre)

    return content


app.run()


