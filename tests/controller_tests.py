from datetime import datetime

import mock
import unittest

from pycin.pycin import Query
from pycinwa.models.models import Movie, Event
from pycinwa.movies.controller import fetch_distinct_movies


class TestMovieController(unittest.TestCase):
    def setUp(self):
        self.movies_to_return = list()
        movie1 = Movie(1, "Test Movie 1", 90, "www.video.li/nk1", "www.poster.li/nk1", dict())
        movie2 = Movie(2, "Test Movie 2", 120, "www.video.li/nk2", "www.poster.li/nk2", dict())
        self.movies_to_return.append(movie1)
        self.movies_to_return.append(movie2)

        self.events_to_return = list()
        event1 = Event(1, "www.booking.li/nk1", movie1, datetime(2024, 4, 27, 10, 0),
                       None, False, dict())
        event2 = Event(2, "www.booking.li/nk2", movie1, datetime(2024, 4, 27, 12, 0),
                       None, False, dict())
        event3 = Event(3, "www.booking.li/nk3", movie2, datetime(2024, 4, 27, 14, 0),
                       None, False, dict())
        self.events_to_return.append(event1)
        self.events_to_return.append(event2)
        self.events_to_return.append(event3)

    @mock.patch("pycin.fetch_events", return_value=Query(list()))
    def test_fetch_distinct_movies_no_movies_found(self, mock_fetch_events):
        empty_movie_list = fetch_distinct_movies()
        self.assertIsInstance(empty_movie_list, list)
        self.assertEqual(0, len(empty_movie_list))
        self.assertEqual(1, mock_fetch_events.call_count)

    @mock.patch("pycin.fetch_events", return_value=Query([
        Event(1, "www.booking.li/nk1", Movie(1, "Test Movie 1", 90, "www.video.li/nk1", "www.poster.li/nk1", dict()),
              datetime(2024, 4, 27, 10, 0),
              None, False, dict()),
        Event(2, "www.booking.li/nk2", Movie(2, "Test Movie 2", 120, "www.video.li/nk2", "www.poster.li/nk2", dict()),
              datetime(2024, 4, 27, 14, 0),
              None, False, dict())
    ]))
    def test_fetch_distinct_movies_movies_found(self, mock_fetch_events):
        empty_movie_list = fetch_distinct_movies()
        self.assertIsInstance(empty_movie_list, list)
        self.assertEqual(len(self.movies_to_return), len(empty_movie_list))
        self.assertEqual(1, mock_fetch_events.call_count)


if __name__ == '__main__':
    unittest.main()
