from flask import Blueprint, jsonify, Response, request

from venus.db import movies

api_movies = Blueprint('movies_blueprint', __name__)


@api_movies.route("/movies", methods = ['GET', 'POST'])
def all_movies():
    """
    Return a list including all movies
    """
    if request.method == 'GET':
        return str(movies)
    else:
        existing_ids = sorted([movie["id"] for movie in movies])
        last_id = existing_ids[-1]
        last_id += 1
        movie_info = request.values.to_dict()
        movie_info["id"] = last_id
        movies.append(movie_info)
        return ""


@api_movies.route("/movies/<int:number>")
def route_number(number):
    """
    Return a specific movie, provided the id
    """
    for movie in movies:
        if movie['id'] == number:
            return str(movie)
