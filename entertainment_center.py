import media
import fresh_tomatoes
 #create an instance of the movie toy_story
toy_story  = media.Movie ('Toy_Story',
                         'A story of a boy whose toys come to life',
                         'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                         'https: // www.youtube.com / watch?v = KYz2wyBy3kc')
 #create an instance of the movie avatar
avatar     = media.Movie('Avatar',
                         'A paraplegic ex-marine finds a new life on the distant planet of Pandora',
                         'https://www.movieposter.com/posters/archive/main/98/MPW-49246',
                         'https://www.youtube.com/watch?v=5PSNL1qE6VY')
 #create an instance of the movie  Conjuring 2
conjuring2 = media.Movie('Conjuring 2',
                         'Ed and Lorrain explore the Enfield Poltergeist tale in London 1973',
                         'http://www.impawards.com/2016/posters/conjuring_two_ver3.jpg',
                         'https://www.youtube.com/watch?v=KyA9AtUOqRM')
 #create an instance of the movie Tarzan
tarzan     = media.Movie('Tarzan',
                         'Tarzan is given the task of abolishing slavery and save Jane',
                         'http://www.impawards.com/2016/posters/tarzan_ver4.jpg',
                         'https://www.youtube.com/watch?v=5PSNL1qE6VY')
 #create an instance of the movie titanic
titanic    = media.Movie('Titanic',
                         'The Journey of Jack and Rose ',
                         'http://movieposters2.com/images/728486-b.jpg',
                         'https://www.youtube.com/watch?v=2e-eXJ6HgkQ')
 #create an instance of the movie frozen
frozen     = media.Movie('Frozen',
                         'The story of two sisters',
                         'https://s-media-cache-ak0.pinimg.com/564x/4e/cc/3f/4ecc3fca4348d86904c75420d2c8fb81.jpg',
                         'https://www.youtube.com/watch?v=TbQm5doF_Uc')

movies=[toy_story,avatar,conjuring2,tarzan,titanic,frozen] #create a list of movies
fresh_tomatoes.open_movies_page(movies)  # open the movies_page using the fresh_tomatoes.py html file