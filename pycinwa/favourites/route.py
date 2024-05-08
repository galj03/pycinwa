from datetime import datetime, timedelta

from flask import Blueprint, render_template

from pycin import fetch_events

favourites = Blueprint('favourites', __name__, static_folder='static', template_folder='templates',
                       url_prefix='/favourites')


@favourites.get('/')
def load_favourites():
    query = fetch_events([datetime.today() + timedelta(days=1)])
    result = list(
        query
        .select(lambda e: e)
    )
    return render_template("favourites.html")
