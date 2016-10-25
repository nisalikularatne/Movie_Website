import webbrowser #import the webbrowser module to open the webbrowser when required
class Movie:      #define a class named Movie

    # constructor for initializing values
    def __init__(self,title,story_line,poster_image,trailer_youtube_url):#constructor for initializing values
        self.title=title
        self.movie_story_line=story_line
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube_url

    #function to display the trailer when clicked on the poster_image
    def Show_Trailer(self):
        webbrowser.open(self.trailer_youtube_url)