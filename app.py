import os
import uuid

from flask import Flask, redirect, url_for, session
from flask_session import Session
from pycinwa.error.route import error
from pycinwa.main.route import main
from pycinwa.watchlist.route import watchlist
from pycinwa.movies.route import movies

app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex

# register blueprints
app.register_blueprint(main)
app.register_blueprint(error)
app.register_blueprint(watchlist)
app.register_blueprint(movies)

# code source: https://www.codeunderscored.com/upload-download-files-flask/
# Creating the upload folder
upload_folder = os.getcwd() + "/uploads/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

# Set's the session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    """ Redirects to the main page.

        :return: Redirects to the main page.
        """
    session['UPLOAD_FOLDER'] = upload_folder
    if session.get('watchlist') is None or session.get('watchlist') == '':
        session['watchlist'] = list()
    return redirect(url_for('main.load_main'))


@app.route('/event-planner')
def watchlist():
    """ Redirects to the watchlist page.

            :return: Redirects to the watchlist page.
        """
    session['UPLOAD_FOLDER'] = upload_folder
    return redirect(url_for('watchlist.load_watchlist'))


@app.route('/show-movies')
def movies():
    """ Redirects to the movies page.

            :return: Redirects to the movies page.
        """
    session['UPLOAD_FOLDER'] = upload_folder
    return redirect(url_for('movies.load_movies'))


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error.load_error',
                            name="HTTP 404 - Not Found",
                            description="Web URL not found."))


@app.errorhandler(500)
def internal_server_error(e):
    return redirect(url_for('error.load_error',
                            name="HTTP 500 - Internal Server Error",
                            description="Something went wrong."))


if __name__ == '__main__':
    app.run()
