import webbrowser


class Movie:
    """Class that represents a movie

    Attributes:
        title (str): The title of the movie.
        storyline (str): The story description of the movie.
        poster_image_url (str): A link to an image of the movie's poster.
        trailer_youtube_url (str): YouTube link for the movie trailer.

    Methods:
        show_trailer: Opens a browser with the YouTube trailer of the movie.
    """
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens a browser with the YouTube trailer of the movie.

        Returns:
        None.
        """
        webbrowser.open(self.trailer_youtube_url)
