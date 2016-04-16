#title, storyline, poster_image, trailer_youtube
#Google python style guide states the first letter should be capital
import webbrowser
class Movie () :
    """This class provides a way to store movie related info"""

def __init__(self, movie_title, movie_storyline,
        poster_image, trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)



