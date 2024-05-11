import os.path
import uuid
from datetime import timedelta, datetime

from flask import session, send_from_directory
from icalendar import Calendar, Event

from pycinwa.models import models


class WatchlistController:
    def __init__(self):
        self.watchlist: list = list() if session.get('watchlist') is None else session['watchlist']
        # consider using session only

    def get_all(self):
        return self.watchlist

    def add_to_list(self, event):
        if not isinstance(event, models.Event):
            raise TypeError('Event must be an instance of Event')
        self.watchlist.append(event)
        session['watchlist'] = self.watchlist

    def remove_from_list(self, event_id):
        event = [event for event in self.watchlist if event.id == event_id][0]

        if event not in self.watchlist:
            raise ValueError('Event not in watchlist')
            # consider just returning here
        self.watchlist.remove(event)
        session['watchlist'] = self.watchlist

    def reset(self):
        self.watchlist.clear()
        session['watchlist'] = self.watchlist

    def export(self):
        cal = Calendar()
        cal.add('prodid', '-//Movies to watch//pycinwa//')
        cal.add('version', '2.0')

        for event in self.watchlist:
            calendar_event = Event()
            calendar_event.add('summary', event.movie.name)
            calendar_event.add('dtstart', event.date)
            calendar_event.add('dtend', event.date + timedelta(minutes=event.movie.length))
            calendar_event.add('dtstamp', datetime.utcnow())
            calendar_event.add('uid', str(uuid.uuid4()))

            cal.add_component(calendar_event)

        filename = 'watchlist.ics'
        with open(os.path.join(session['UPLOAD_FOLDER'], filename), 'wb') as fp:
            fp.write(cal.to_ical())

        return send_from_directory(session['UPLOAD_FOLDER'], filename)
