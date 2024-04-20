from flask import Flask
from datetime import datetime

# TODO: write these myself :(
import collections.abc
collections.Iterable = collections.abc.Iterable
from pycin import fetch_events

app = Flask(__name__)


# TODO: list pycin stuff
@app.route('/')
def index():  # put application's code here
    return fetch_events([datetime.today()])


# TODO: plan events, export into some datetime format
@app.route('/event-planner')
def event_planner():  # put application's code here
    return 'Hello World!'


# TODO: edit config data (fav. cinemas, settings, etc.)
@app.route('/config')
def config():  # put application's code here
    return 'Hello World!'


# TODO: find use for a 4th page

if __name__ == '__main__':
    app.run()
