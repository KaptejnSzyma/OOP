class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration):
        """Song init method

        Args:
            title (str): Initializes the 'title' attribute
            artist (Artist): An artist object representing the song's creator
            duration (Optional[int]): Initial value for the 'duration' attribute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)