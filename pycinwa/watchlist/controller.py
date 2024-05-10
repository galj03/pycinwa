from flask import session

from pycinwa.models.models import Event


class WatchlistController:
    def __init__(self):
        self.watchlist: list = list() if session.get('watchlist') is None else session['watchlist']
        # consider using session only

    def get_all(self):
        return self.watchlist

    def add_to_list(self, event):
        if not isinstance(event, Event):
            raise TypeError('Event must be an instance of Event')
        self.watchlist.append(event)
        session['watchlist'] = self.watchlist

    def remove_from_list(self, event_id):
        event = [event for event in self.watchlist if event.id == event_id][0]

        if not isinstance(event, Event):
            raise TypeError('Event must be an instance of Event')
        if event not in [self.watchlist]:
            raise ValueError('Event not in watchlist')
            # consider just returning here
        self.watchlist.remove(event)
        session['watchlist'] = self.watchlist

    def reset(self):
        self.watchlist.clear()
        session['watchlist'] = self.watchlist
