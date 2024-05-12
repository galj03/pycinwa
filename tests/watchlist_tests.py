import unittest
from datetime import datetime

from flask import url_for

from app import app
from pycinwa.models.models import Movie, Event


# TODO: only implement if there is enough time for it


class TestWatchlistController(unittest.TestCase):
    # @mock.patch("flask.session.get", return_value=list())
    def setUp(self):
        self.app = app.test_client()

        movie1 = Movie(1, "Test Movie 1", 90, "www.video.li/nk1", "www.poster.li/nk1", dict())
        movie2 = Movie(2, "Test Movie 2", 120, "www.video.li/nk2", "www.poster.li/nk2", dict())

        event1 = Event(1, "www.booking.li/nk1", movie1, datetime(2024, 5, 27, 10, 0),
                       None, False, dict())
        event2 = Event(2, "www.booking.li/nk2", movie1, datetime(2024, 5, 27, 12, 0),
                       None, False, dict())
        event3 = Event(3, "www.booking.li/nk3", movie2, datetime(2024, 5, 27, 14, 0),
                       None, False, dict())
        watchlist = list()
        watchlist.append(event1)
        watchlist.append(event2)
        watchlist.append(event3)

        self.watchlist = watchlist

    def test_get_all(self):
        # app.app_context()
        with app.test_client() as client:
            with app.test_request_context():
                with client.session_transaction() as session:
                    session['watchlist'] = self.watchlist
                response = client.get(url_for('watchlist.load_watchlist'))
                assert response.data == 'uid in session'

        # all_events = self.controller.get_all()
        # self.assertEqual(3, len(all_events))
        # for i in range(len(all_events)):
        #     self.assertIsInstance(all_events[i], Event)
        #     self.assertEqual(self.watchlist[i].id, all_events[i].id)


if __name__ == '__main__':
    unittest.main()
