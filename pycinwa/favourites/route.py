from datetime import datetime, timedelta

from flask import Blueprint, render_template

from pycin import fetch_events, CINEMAS
from pycinwa.asd import fetch_distinct_movies

favourites = Blueprint('favourites', __name__, static_folder='static', template_folder='templates',
                       url_prefix='/favourites')


@favourites.get('/')
def load_favourites():
    query = fetch_events([datetime.today() + timedelta(days=1)])
    result = list(
        query
        .select(lambda e: e)
    )
    mov = fetch_distinct_movies()
    return render_template("favourites.html")
