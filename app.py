from flask import Flask, render_template
from datetime import datetime
from pycin.pycin import fetch_events

app = Flask(__name__)


# TODO: filtering
@app.route('/')
def index():  # put application's code here
    query = fetch_events([datetime.today()])
    result = list(
        query
        .select(lambda e: e)
    )
    # TODO: get unique cinema list
    cinemas = list(query.filter(lambda e: e not in query)
                   .select(lambda e: e))
    return render_template("index.html", fetched_data=result, fetched_cinemas=cinemas)


# TODO: plan events, export into some datetime format
    # TODO: only the exportation and showing should be done here
    # TODO: adding to planned will be on the main page
    # TODO: list favourite movies
@app.route('/event-planner')
def event_planner():  # put application's code here
    return 'Hello World!'


# TODO: edit config data (fav. cinemas, settings, etc.)
    # filters could go here? (no reason btw)
@app.route('/config')
def config():  # put application's code here
    return 'Hello World!'


@app.route('/login')
def favourites():  # put application's code here
    return render_template('login.html')

#TODO: get the trailers from somewhere (port.hu/YT)
    #see where cinema city gets it from
    #an iframe could work


if __name__ == '__main__':
    app.run()
