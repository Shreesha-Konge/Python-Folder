#Movie
class Movie:
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.rating=rating
    def __str__(self):
        return f'Movie Title:{self.title}\nDirector:{self.director}'
    def __len__(self):
        return f'Rating:{self.rating}'
m=Movie('HAHK','YashRaj',5.0)
print(m)
print(str(m))
print(len(m))

        
        