from flask import Blueprint, render_template

from pycinwa.asd import fetch_distinct_movies

error = Blueprint('error', __name__, static_folder='static', template_folder='templates',
                  url_prefix='/error')


@error.get('/')
def error():
    # TODO: params
    mov = fetch_distinct_movies()
    return render_template("error.html")
