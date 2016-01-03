import webbrowser

class Movie(object):

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_url, movie_reviews=''):
		self.title = movie_title
		self.trailer_youtube_url = trailer_url
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.reviews = movie_reviews

	def show_trailer(self):
		webbrowser.open(self.youtube_trailer_url)