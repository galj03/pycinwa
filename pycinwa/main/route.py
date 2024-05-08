from datetime import datetime, timedelta

from flask import Blueprint, render_template

from pycin import fetch_events, CINEMAS

main = Blueprint('main', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/main')


# TODO: filtering
@main.get('/')
def load_main():
    query = fetch_events([datetime.today() + timedelta(days=1)])
    result = list(
        query
        .select(lambda e: e)
    )
    return render_template("index.html", fetched_data=result, fetched_cinemas=CINEMAS)
