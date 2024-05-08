from flask import Blueprint, render_template

from pycinwa.movies.controller import fetch_distinct_movies

movies = Blueprint('movies', __name__, static_folder='static', template_folder='templates',
                   url_prefix='/movies')


@movies.get('/')
def load_movies():
    # TODO: params
    mov = fetch_distinct_movies()
    return render_template("movies.html")
