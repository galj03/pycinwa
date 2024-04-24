from flask import Flask, render_template
from datetime import datetime, timedelta
from pycin.pycin import fetch_events, CINEMAS

app = Flask(__name__)


# TODO: filtering
@app.route('/')
def index():
    query = fetch_events([datetime.today() + timedelta(days=1)])
    result = list(
        query
        .select(lambda e: e)
    )
    return render_template("index.html", fetched_data=result, fetched_cinemas=CINEMAS)


# TODO: plan events, export into some datetime format
# TODO: only the exportation and showing should be done here
# TODO: adding to planned will be on the main page
# TODO: list favourite movies
@app.route('/event-planner')
def event_planner():
    return 'Hello World!'


# TODO: edit config data (fav. cinemas, settings, etc.)
# filters could go here? (no reason btw)
@app.route('/config')
def config():
    return 'Hello World!'


@app.route('/login')
def favourites():
    return render_template('login.html')


# TODO: get the trailers from somewhere (port.hu/YT)
# see where cinema city gets it from
# an iframe could work


if __name__ == '__main__':
    app.run()
