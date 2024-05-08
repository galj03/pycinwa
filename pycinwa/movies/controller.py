from datetime import datetime

from pycin import fetch_events


def fetch_distinct_movies(date=datetime.today()) -> list:
    events = fetch_events([date])
    # movies = events.filter(lambda event: event[''] == date)
    movies = list()
    for event in events.select(lambda e: e):
        if event.movie not in movies:
            movies.append(event.movie)
    return movies
