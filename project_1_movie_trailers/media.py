########################################################################
# Project 1: Movie Trailer Website
# Date Completed: 12/6/2016
# Submitted by: Linda Zhang
########################################################################

############################## Media File ##############################
# This module creates the class Movie to allow for its use in the
# entertainment_center.py module. This definition of the class Movie
# was obtained through the course.
########################################################################

class Movie():
    """This class provides a way to store movie-related information"""

    # A movie instance will have the following properties
    def __init__(self, movie_title, movie_storyline, movie_rating,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
