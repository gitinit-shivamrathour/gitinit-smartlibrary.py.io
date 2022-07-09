from mimetypes import init
from secrets import choice
from time import sleep
import os
# i cant believe in that this created by me , ha ha ha ha

class Student:
    def requestBook(self):
        self.bookname = input("\n\t\tEnter the name of the book: ")
        return self.bookname

    def returnBookreq(self):
        self.bookname = input("\n\t\tEnter the unique Name of book: ")
        self.bookid = input("\n\t\tEnter the unique id of book: ")
        
        listbookid = [self.bookname, self.bookid]
        return listbookid


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.copy = tuple(listOfBooks.values())

    def displayListOfBooks(self):
        print("\n\n\t*-----The books, available in the library are-----*")

        for book, id in self.books.items():
            print("\n\t\t -> "+ f"{book}: {id}")

    def borrowBook(self, bookName):
        if bookName in self.books or bookName in self.books.values():
            print(f"\n\t\t{bookName} have been issued to you, keep it safe and return on time.")
            self.books.pop(bookName)
            return True
        else:
            print("\n\t\tThis book is not available at this time or have been issued to someother person")
            return False

    def returnBook(self, listbookid):
        if listbookid[1] not in self.books.values():
            if listbookid[1] in self.copy:
                self.books.update({f'{listbookid[0]}': f'{listbookid[1]}'})
                print("\n\t\tthanks for returning the book on time, now you can borrow another book from the library.")
            else:
                print("\n\t\tinvalid id")
        else:
            print("\n\t\tplease try again & enter a valid book id!")


if __name__ == "__main__":
    centralLibrary = Library({"docpy":"3425", "pyspark":"6578", "pytorch":"2547", "scipy":"9854", "numpy":"7808", "pandas":"3214"})
    stukid = Student()

    while(True):
        startmsg = ('''\n\n\t*----------------Central Library----------------*
        
                Please choose an option, you want:
        
                1. List all Available books.
                2. Request a book.
                3. Return a book.
                4. Exit the Library.
        ''')

        print(startmsg)

        try:
            choice = int(input("\n\t\tEnter a choice: "))
            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError as e:
            print(
                f"\n\t\tA ValueError /{e}/ is arrived, please enter a choice as number: ")

        if choice == 1:
            centralLibrary.displayListOfBooks()
            sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == 2:
            centralLibrary.borrowBook(stukid.requestBook())
            sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == 3:
            centralLibrary.returnBook(stukid.returnBookreq())
            sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\t\tthanks for using our services.\n")
            sleep(2)
            exit()
        else:
            print("\n\t\tPlease enter a valid choice!")
            sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
