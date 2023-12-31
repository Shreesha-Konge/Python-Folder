#class to represent book with attributes
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def display_info(self):
        return f'Title : {self.title}\nAuthor : {self.author}\nYear : {self.year}'
B1=Book('Python','Jose',2005)
B2=Book('Java','James',2003)
print(B1.display_info())
print(B2.display_info())


        