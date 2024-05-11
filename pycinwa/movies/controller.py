from datetime import datetime

import pycin


# from pycin import fetch_events


def fetch_distinct_movies(date=datetime.today()) -> list:
    """
    Fetches distinct movies which are on air in Hungarian Cinema City cinemas

    Parameters
    ----------
    date: the date from which we want to fetch distinct movies

    Returns
    -------
    a list of distinct movies
    """
    events = pycin.fetch_events([date])
    movies = list()
    for event in events.select(lambda e: e):
        if event.movie not in movies:
            movies.append(event.movie)
    return movies
