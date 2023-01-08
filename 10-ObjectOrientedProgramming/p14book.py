class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.status = False

    def openbook(self):
        self.status = True

    def closebook(self):
        self.status = False

    def displaystatus(self):
        print(self.title, self.author, self.pages, self.current_page)

    def readbook(self):
        if self.status:
            self.current_page += 1
        else:
            print("The book is closed")

    
# b = Book("Tytul","Autor", 100)
# b.openbook()
# b.displaystatus()
# b.readbook()
# b.readbook()
# b.readbook()
# b.displaystatus()
# b.closebook()
# b.readbook()


# b.	Open a book
# c.	Display a book status (title, author, page numbers, current page no)
# d.	Read a few pages
# e.	Display a book status
# f.	Close a book
# g.	Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).
