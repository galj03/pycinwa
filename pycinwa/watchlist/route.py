from flask import Blueprint, render_template, redirect, url_for

from pycinwa.watchlist.controller import WatchlistController

watchlist = Blueprint('watchlist', __name__, static_folder='static',
                      template_folder='templates',
                      url_prefix='/watchlist')


@watchlist.get('/')
def load_watchlist():
    """
    Loads the watchlist page

    Returns
    -------
    The watchlist page, with the following content:
    watchlist: the items added to the watchlist
    """
    _watchlist_controller = WatchlistController()
    return render_template("watchlist.html",
                           watchlist=_watchlist_controller.get_all())


@watchlist.post('/reset')
def reset():
    """
    Resets the watchlist

    Redirects to the watchlist page
    """
    _watchlist_controller = WatchlistController()
    _watchlist_controller.reset()
    return redirect(url_for('watchlist.load_watchlist'))


@watchlist.post('/export')
def export():
    """
    Exports the watchlist to an ics file
    (importable for calendars - ex. Google Calendar)

    Downloads the exported file
    """
    _watchlist_controller = WatchlistController()
    return _watchlist_controller.export()
