import json
import sqlite3


def get_by_title(user_query):
    """" Функция, с помощью которой получаем список с фильмами по названию """

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:

        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, country, release_year, listed_in as genre, description
                FROM netflix
                WHERE title LIKE '%{user_query}%'
                ORDER BY release_year DESC
                LIMIT 1
                """
        cursor.execute(query)
        executed_query = cursor.fetchall()

        # результат в установленном формате
        result = {
            'title': executed_query[0][0],
            'country': executed_query[0][1],
            'release_year': executed_query[0][2],
            'genre': executed_query[0][3],
            'description': executed_query[0][4]
        }

    json_result = json.dumps(result)

    return json_result


def get_by_year(year_no_1, year_no_2):
    """Функция, с помощью которой получаем список фильмов в диапазоне годов выпуска"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:

        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN '{year_no_1}' AND '{year_no_2}'
                ORDER BY release_year DESC
                LIMIT 100
                """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'release_year': row[1],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result


def get_children():
    """Функция, с помощью которой получаем фильмы для детей"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:
        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating='G'
                ORDER BY title ASC
                """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'rating': row[1],
                'description': row[2],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result


def get_family():
    """Функция, с помощью которой получаем фильмы для семейного просмотра"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:
        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating='G' OR rating='PG' OR rating='PG-13'
                ORDER BY title ASC
                """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'rating': row[1],
                'description': row[2],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result


def get_adult():
    """Функция, с помощью которой получаем фильмы для взрослых"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:
        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating='R' OR rating='NC-17'
                ORDER BY title ASC
                """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'rating': row[1],
                'description': row[2],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result


def get_by_genre(genre):
    """Функция, с помощью которой получаем фильмы по жанру"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:
        result = {}

        cursor = connection.cursor()
        query = f"""
                SELECT title, description, release_year
                FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10
                """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'description': row[1],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result


def get_actors(actor_1, actor_2):
    """Функция, с помощью которой получаем в качестве аргумента имена двух актеров, сохраняем всех актеров из колонки cast и возвращаем список тех, кто играет с ними в паре больше 2 раз"""

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT COUNT(`cast`), `cast`
                FROM netflix
                WHERE `cast` LIKE '%{actor_1}%' AND `cast` LIKE '%{actor_2}%'
                GROUP BY `cast`
                """
        cursor.execute(query)

        return cursor.fetchall()


def find_content(type_film, year, genre):
    """Функция, с помощью которой получаем фильм по указанным в запросе характеристикам (тип, год выпуска, жанр)"""

    list_with_films = []

    # подключение к базе данных
    with sqlite3.connect('netflix.db') as connection:
        result = {}

        cursor = connection.cursor()
        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE `type` LIKE '%{type_film}%' AND release_year='{year}' AND listed_in LIKE '%{genre}%'
                    ORDER BY title ASC
                    """
        cursor.execute(query)

        for row in cursor.fetchall():

            # результат в установленном формате
            result = {
                'title': row[0],
                'description': row[1],
            }
            list_with_films.append(result)

    json_result = json.dumps(list_with_films)

    return json_result
