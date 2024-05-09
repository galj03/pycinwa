from datetime import datetime


class Cinema:
    """
    A class used to represent a Cinema

    ...

    Attributes
    ----------
    id : str
        unique identifier
    name : str
        name of the cinema

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Movie:
    """
    A class used to represent a Movie

    ...

    Attributes
    ----------
    id : str
        unique identifier
    name : str
        name(title) of the movie(film)
    length : int
        length of the movie in minutes
    video_link : str
        the youtube link of the movie trailer
    poster_link : str
        the link for the movie poster
    attributes : list
        collection of strings containing attribute keywords

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, id, name, length, video_link, poster_link, attributes):
        self.id = id
        self.name = name
        self.length = length
        self.attributes = attributes
        self.poster_link = poster_link
        self.video_link = self._make_video_embeddable(video_link)

    @staticmethod
    def _make_video_embeddable(video_link: str):
        embeddable_link = video_link.replace('watch?v=', 'embed/')
        return embeddable_link


class Event:
    """
    A class used to represent an Event

    ...

    Attributes
    ----------
    id : str
        unique identifier
    booking_link : str
        url for the booking link
    movie : Movie
        object of the movie
    cinema : Cinema
        object of the cinema
    date : datetime
        the date of the event
    sold_out : bool
        boolean signaling the availability of tickets
    attributes : list
        collection of strings containing attribute keywords

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, id, booking_link, movie, date, cinema, sold_out, attributes):
        self.id = id
        self.booking_link = booking_link
        self.movie = movie
        self.date = date
        self.cinema = cinema
        self.sold_out = sold_out
        self.attributes = attributes
