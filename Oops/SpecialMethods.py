class Book():
    def __init__(self,book,author,pages):
        self.book=book
        self.author=author
        self.pages=pages
    def __str__(self):
        return f'{self.book} by {self.author} and it has {self.pages}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('This object has been deleted')
b=Book('Python Rocks','Jose',200)
print(b)
print(str(b))
print(len(b))
del b
        