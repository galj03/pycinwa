from flask import Blueprint, render_template, redirect, url_for

from pycinwa.watchlist.controller import WatchlistController

watchlist = Blueprint('watchlist', __name__, static_folder='static', template_folder='templates',
                      url_prefix='/watchlist')


@watchlist.get('/')
def load_watchlist():
    _watchlist_controller = WatchlistController()
    return render_template("watchlist.html", watchlist=_watchlist_controller.get_all())


@watchlist.post('/reset')
def reset():
    _watchlist_controller = WatchlistController()
    _watchlist_controller.reset()
    return redirect(url_for('watchlist.load_watchlist'))


@watchlist.post('/export')
def export():
    _watchlist_controller = WatchlistController()
    return _watchlist_controller.export()
    # return redirect(url_for('watchlist.load_watchlist'))
