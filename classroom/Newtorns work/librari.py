import sys

class Library:
    def __init__(self,listofbooks):
        self.availablebooks = listofbooks
        
        
    def displayavailablebooks(self):
        print("the books we have in our library are as follows")
        print("-----------------------------------------------")
        for book in self.availablebooks:
            print(book)
            
    def borrowabook(self,requestedbook):
        if requestedbook in self.availablebooks:
            print("the book you have requested has now been borrowed")
        else:
            print("sorry the book you have requested is currently not in the library")
            
    def addbook(self,returnedbooks):
        self.availablebooks.append(returnedbook)
        print("thank you for returing your borrowed book")
Library()         
class Student:
    def requestbook(self):
        print("enter the name  of the book you like to borrow")
        self.book = input()
        return self.book
    
    def returnbook(self):
        print("enter the name of the book you would like to return")
        self.book = input()
        return self.book
Student()               
def main():
    library = Library(
        ["diary of a wimpy kid","captain under pance"," the tortoice and th hare"])
    student = Student()
    done=False
    
    while done==False:
        print('''=====LIBRARY MANU=====
            1. display all available books
            2. recwest a book
            3. return a book
            4. Exit
            ''')
        
        choice = int(input("enter choice: "))

        if choice == 1:
            library.displayavailablebooks()

        elif choice == 2:
            library.borrowabook(student.requestbook())

        elif choice == 3:
            library.addbook(student.returnbook())

        elif choice == 4:
            sys.exit()
        
main()        