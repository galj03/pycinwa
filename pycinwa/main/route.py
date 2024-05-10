from datetime import datetime, timedelta

from flask import Blueprint, render_template, redirect, url_for, session

from pycin import fetch_events, CINEMAS
from pycinwa.watchlist.controller import WatchlistController

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
    asd = session['watchlist']
    session['fetched'] = result
    return render_template("index.html", fetched_data=result, fetched_cinemas=CINEMAS)


@main.get('/api/remove-from-watchlist/<event_id>')
def remove_from_watchlist(event_id):
    _watchlist_controller = WatchlistController()
    _watchlist_controller.remove_from_list(event_id)
    return redirect(url_for('main.load_main'))


@main.get('/api/add-to-watchlist/<event_id>')
def add_to_watchlist(event_id):
    fetched = session['fetched']
    # TODO: export this into a function/method
    event = [event for event in fetched if event.id == event_id][0]

    _watchlist_controller = WatchlistController()
    _watchlist_controller.add_to_list(event)
    return redirect(url_for('main.load_main'))
