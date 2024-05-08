from flask import Flask, redirect, url_for
from flask_session import Session
from pycinwa.error.route import error
from pycinwa.main.route import main
from pycinwa.favourites.route import favourites
from pycinwa.movies.route import movies

app = Flask(__name__)

# register blueprints
app.register_blueprint(main)
app.register_blueprint(error)
app.register_blueprint(favourites)
app.register_blueprint(movies)

# Set's the session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    """ Redirects to the main page.

        :return: Redirects to the main page.
        """
    return redirect(url_for('main.load_main'))


# TODO: move these into their own places

# TODO: plan events, export into some datetime format
# TODO: only the exportation and showing should be done here
# TODO: adding to planned will be on the main page (using session)
# TODO: list favourite movies
@app.route('/event-planner')
def favourites():
    return 'Hello World!'


# TODO: list all movies and trailers
@app.route('/movies')
def config():
    return 'Hello World!'


# TODO: get the trailers from movie object
# an iframe could work


if __name__ == '__main__':
    app.run()
