class Library:
    def __init__(self,availableBooks):
        self.availableBooks=availableBooks
    def displayAvailableBooks(self):
        print("The requested books are")
        for books in self.availableBooks:
            print()
            print(books)
    def lendBooks(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have requested {} book and is processed".format(requestedBook))
            self.availableBooks.remove(requestedBook)
        else:
            print('Sorry we do not have the book')
    def addBooks(self,returnedBook):
        self.availableBooks.append(returnedBook)
class Customer:
    def requestBooks(self):
        print('Enter the book you want to request from the library')
        self.requestedBook=input()
        return(self.requestedBook)
    def returnBooks(self):
        print('Enter the book you want to return')
        self.returnedBook=input()
        return self.returnedBook
library=Library(['Who will cry when you Die','Rich Dad Poor Dad','Girl in the Train'])
customer=Customer()
while True:
    print()
    print("Enter the choice for the Library")
    print("1.Display books")
    print("2.Request a book")
    print("3.Return a book")
    print("4.Quit")
    choice=int(input())
    if(choice==1):
        library.displayAvailableBooks()
    elif(choice==2):
        requestedBook=customer.requestBooks()
        library.lendBooks(requestedBook)
    elif(choice==3):
        returnedBook=customer.returnBooks()
        library.addBooks(returnedBook)
    else:
        quit()
