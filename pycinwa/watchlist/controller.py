import os.path
import uuid
from datetime import timedelta, datetime

import flask
from flask import session, send_from_directory
from icalendar import Calendar, Event

from pycinwa.models import models


class WatchlistController:
    """
    The controller class for the Watchlist module

    ...

    Attributes
    ----------
    watchlist : list
        a list containing all events added to watchlist
        (the list is initialized from session variable)

    Methods
    -------
    get_all()
        Returns all events added to the watchlist
    add_to_list(event)
        adds a new event to the watchlist
        (raises TypeError when event is not a models.Event object)
    remove_from_list(event_id)
        removes the event with given id from the watchlist
        (raises ValueError when event is not present in the watchlist)
    reset()
        Clears the watchlist
    export()
        Exports the watchlist to an ics file, and downloads it
    """

    def __init__(self):
        self.watchlist: list = list() if 'watchlist' not in session else session['watchlist']

    def get_all(self):
        """
        Returns all events added to the watchlist

        Returns
        -------
        All models.Event objects added to the watchlist
        """
        return self.watchlist

    def add_to_list(self, event):
        """
        Adds a new event to the watchlist
        (also updates session variable)

        Parameters
        ----------
        event: models.Event
            the event to be added to the watchlist
        """
        if not isinstance(event, models.Event):
            raise TypeError('Event must be an instance of Event')
        self.watchlist.append(event)
        session['watchlist'] = self.watchlist

    def remove_from_list(self, event_id):
        """
        Removes the event with given id from the watchlist
        (also updates session variable)

        Parameters
        ----------
        event_id: int
            the id of the event to be removed
        """
        try:
            event = [event for event in self.watchlist if event.id == event_id][0]
        except IndexError:
            raise IndexError('Event not present in the watchlist')

        if event not in self.watchlist:
            raise ValueError('Event not in watchlist')
            # consider just returning here
        self.watchlist.remove(event)
        session['watchlist'] = self.watchlist

    def reset(self):
        """
        Clears the watchlist
        (also updates session variable)
        """
        self.watchlist.clear()
        session['watchlist'] = self.watchlist

    def export(self):
        """
        Exports the watchlist to an ics file, and downloads it

        Returns
        -------
        The flask response to download the exported file
        """
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
