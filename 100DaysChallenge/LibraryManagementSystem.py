#Library Management System
class Library1:
  books = []
  no_of_books = 0
  def addBook(self,bName):
    self.books.append(bName)
    self.no_of_books = len(self.books)
  def showbooks(self):
    print("Book added in Library successfully!!")
    print(f"Total number of books in shelf are {self.no_of_books} and the books are ")
    for book in self.books:
      print(book)

a = Library1()
a.addBook("The Alchemist")
a.addBook("Time Management")
a.addBook("Visual Studio Management")
a.showbooks()
