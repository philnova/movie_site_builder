import movie
import movie_site_builder
import random

toy_story = movie.Movie("Toy Story", 
	"A story of a boy and toys that come to life", 
	"http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#toy_story.show_trailer()

def parse_movie_file(filename):
	movie_array = []
	with open(filename) as fo:
		for idx, line in enumerate(fo):
			if idx: #ignore first line
				line_array = line.split("\t")
				title, summary, poster, trailer = line_array[0], line_array[1], line_array[2], line_array[3]
				current_movie = movie.Movie(title, summary, poster, trailer)
				print title, summary, poster, trailer
				movie_array.append(current_movie)
	random.shuffle(movie_array)
	return movie_array

movie_site_builder.open_movies_page(parse_movie_file("movie_db.txt"))
