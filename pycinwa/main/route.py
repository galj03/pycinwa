from datetime import datetime, timedelta

from flask import Blueprint, render_template, redirect, url_for, session, request

from pycin import fetch_events, CINEMAS
from pycin.pycin import DATE_FORMAT
from pycinwa.watchlist.controller import WatchlistController

main = Blueprint('main', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/main')


# TODO: filtering
@main.get('/')
def load_main():
    args = request.args
    date = datetime.today() + timedelta(days=1)
    if args.get('date') is not None and args['date'] != '':
        date = datetime.strptime(
            args['date'], DATE_FORMAT)
    query = fetch_events([date])
    result = list(
        query
        .select(lambda e: e)
    )
    result = apply_filters(result, args)
    session['fetched'] = result
    return render_template("index.html", fetched_data=result, fetched_cinemas=CINEMAS,
                           watchlist_ids=[event.id for event in session['watchlist']])


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


def apply_filters(events, args: dict):
    if args.get('title') is not None and args['title'] != '':
        events = [event for event in events if args['title'].lower() in event.movie.name.lower()]
    if args.get('max_length') is not None and args['max_length'] != '':
        events = [event for event in events if event.movie.length <= int(args['max_length'])]
    if ((args.get('allCinemas') is None or args['allCinemas'] != '')
            and args.get('cinemas') is not None and args['cinemas'] != ''):
        events = [event for event in events if event.cinema.id == args['cinemas']]
    return events
