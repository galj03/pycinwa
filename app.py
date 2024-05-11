import os

from flask import Flask, redirect, url_for, session
from flask_session import Session
from pycinwa.error.route import error
from pycinwa.main.route import main
from pycinwa.watchlist.route import watchlist
from pycinwa.movies.route import movies

app = Flask(__name__)

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
    return redirect(url_for('main.load_main'))


@app.route('/event-planner')
def watchlist():
    """ Redirects to the watchlist page.

            :return: Redirects to the watchlist page.
        """
    session['UPLOAD_FOLDER'] = upload_folder
    return redirect(url_for('watchlist.load_watchlist'))


@app.route('/movies')
def movies():
    """ Redirects to the movies page.

            :return: Redirects to the movies page.
        """
    session['UPLOAD_FOLDER'] = upload_folder
    return redirect(url_for('movies.load_movies'))


if __name__ == '__main__':
    app.run()
