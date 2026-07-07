class Book:
    def __init__(self,title,author,is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True

    def return_book(self,title):
        self.is_borrowed = False

    def show_status(self,title):
        if self.is_borrowed == False:
            print(f"{self.title} by {self.author} is Availaible")
        else:
            print(f"{self.title} by {self.author} is Not Availaible")

b1 = Book("Twisted Series","Ana Huang")
b2 = Book("Better Than The Movies","Lynn Painter")

b1.borrow()
b1.show_status("Twisted Series")

b1.return_book("Twisted Series")
b1.show_status("Twisted Series")
print()
b2.show_status("Better Than The Movies")
b2.borrow()
b2.show_status("Better Than The Movies")


            
