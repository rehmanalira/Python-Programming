"""
It is a project in whcih we haveing a library of books or class of library in which we can see the
books and add our book and then we can also lend the books and also we return the book


"""
class library:

    def __init__(self,book_list,name): # constructor which take the list of book and name
        self.book_list=book_list
        self.name=name

    def display_books(self): # for displaying the books
        print("We have following books ")
        print(self.book_list)

    def add_books(self): # for adding the books
        name=input("enter what you books want to add")
        self.book_list.append(name)
    def lend_books(self): # lending the books
        print("Enter your name")
        lend_name=str(input())
        print("Enter the book you want to lend")
        lend=str(input())
        if lend in self.book_list: # here we check the book in list if it is avaiblble
            print("Book is Lend successfully")
        elif lend is not self.book_list:
            print("You entered the wrong book")



    def return_book(self):  # returning the book
        print("enter your name")
        return_name=str(input())
        print("Enter the book name")
        return_book=str(input())
        if return_book in self.book_list:
            print("You returned the book")
        else:
            print("You entered wrong book name")
def main():
    books = ["programing" ,"pakistan"] # book list which every object can make its own book list
    ali = library(books, "Ali") # and here we gave the book list and his name

    while ( True ): # while loop
        print(f"\nThis is The Library of {ali.name}")
        print("Press 1 for 'displaying book' 2 for 'adding book' 3 for 'lend a book' 4 for 'returning book' 5 exit ")
        ch = int(input())
        if ch == 1:
            ali.display_books()
        if ch == 2:
            ali.add_books()
        if ch == 3:
            ali.lend_books()
        if ch == 4:
            ali.return_book()
        if ch == 5:
            exit()

if __name__ == '__main__':
    main()
