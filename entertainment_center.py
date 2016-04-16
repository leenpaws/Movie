import Movieclass
import fresh_tomatoes

toy_story = Movieclass.Movie("Toy Story",
                             "A story of a boy and his toys that come to life",
                             "http://s3-us-west-2.amazonaws.com/images.hellogiggles.com/uploads/2014/11/06/" \
                             "Toy-story-coloring-500x375c.jpg",
                             "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movieclass.Movie("Avatar",
                          "Cultural appropriation in space",
                          "http://images2.fanpop.com/image/photos/9400000/movie-poster-avatar-the-movie" \
                          "-9459182-376-500.jpg",
                          "https://www.youtube.com/watch?v=_i2RCBa3l-g")
star_wars = Movieclass.Movie("Star Wars",
                             "Priest kidnaps child for cult and eventual marriage to...." \
                             "politician twice his age",
                             "http://cdn.collider.com/wp-content/uploads/star-wars-episode-1-poster-" \
                             "398x600.jpg",
                             "https://www.youtube.com/watch?v=I6hOlI9cg4o")

matrix = Movieclass.Movie("The Matrix",
                          "A depressed office worker joins a cult and destabilizes the government",
                          "http://images.moviepostershop.com/the-matrix-movie-poster-" \
                          "1999-1010189516.jpg",
                          "https://www.youtube.com/watch?v=_Ls19O-9p3s")

movies = [toy_story, avatar, star_wars, matrix]

fresh_tomatoes.open_movies_page(movies)
