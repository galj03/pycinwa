import mock
import unittest
from datetime import datetime

from pycin.pycin import CinemaEventFactory


class TestCinemaEventFactory(unittest.TestCase):
    def test_create_event(self):
        new_event = CinemaEventFactory.create_event(**{
            'id': 10,
            'movie': 'The Dark Knight',
            'cinema': 2,
            'eventDateTime': '2024-04-27T10:00:00',
            'soldOut': False,
            'bookingLink': 'asd',
            'attributeIds': dict()
        })
        self.assertEqual(new_event.id, 10)
        self.assertEqual(new_event.movie, 'The Dark Knight')
        self.assertEqual(new_event.cinema, 2)
        self.assertEqual(new_event.date, datetime(2024, 4, 27, 10, 0))
        self.assertEqual(new_event.sold_out, False)
        self.assertEqual(new_event.booking_link, 'asd')
        self.assertCountEqual(new_event.attributes, dict())

    def test_create_movie(self):
        new_movie = CinemaEventFactory.create_movie(**{
            'id': 10,
            'name': 'The Dark Knight',
            'length': 152,
            'videoLink': 'https://youtu.be/EXeTwQWrcwY?si=sBpXfHnlUtPQrK8f',
            'attributeIds': dict()
        })
        self.assertEqual(new_movie.id, 10)
        self.assertEqual(new_movie.name, 'The Dark Knight')
        self.assertEqual(new_movie.length, 152)
        self.assertEqual(new_movie.video_link, 'https://youtu.be/EXeTwQWrcwY?si=sBpXfHnlUtPQrK8f')
        self.assertCountEqual(new_movie.attributes, dict())

    def test_create_cinema(self):
        new_cinema = CinemaEventFactory.create_cinema(**{
            'id': 10,
            'displayName': 'Belvarosi Mozi'
        })
        self.assertEqual(new_cinema.id, 10)
        self.assertEqual(new_cinema.name, 'Belvarosi Mozi')


class TestPyCinFunctions(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()

# TODO: make this work from pytest as well :)
