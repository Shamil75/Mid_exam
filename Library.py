
class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title 
        self.__author = author
        self.__availability = availability

    def borrow_book(self):
        if self.__availability == True:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print(f"Error: Book '{self.__title}' is Not Availabile.")

    def return_book(self):
        if self.__availability == False:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print(f"Error: Book '{self.__title}' is not borrowed.")

    def view_book_info(self):
        if self.__availability == True:
            print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: Availabile")
        else:
            print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: Not Availabile")
        
    def book_id(self):
        return self.__book_id

def menu():
    while True:
        print("\n-----Welcome to the Library-----")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print("\nLibrary Books:")
            for book in Library.book_list:
                Book.view_book_info(book)

        elif choice == 2:
            book_id = int(input("Enter Book ID to borrow: "))
            for book in Library.book_list:
                if Book.book_id(book) == book_id:
                    Book.borrow_book(book)
                    break
            else:
                print("Error: Invalid Id")

        elif choice == 3:
            book_id = int(input("Enter Book ID to return: "))
            for book in Library.book_list:
                if Book.book_id(book) == book_id:
                    Book.return_book(book)
                    break
            else:
                print("Error: Invalid ID")
                    
        elif choice == 4:
            print("Exiting the library system...")
            break
        else:
            print("Error: Invalid choice")

book1 = Book(101, 'Moyerakkhe', 'Humayon Ahamed', True)
book2 = Book(102, 'Deyel ar Opashe', 'Humayon Ahamed', True)
book3 = Book(103, 'Lilabotir Mittu', 'Humayon Ahamed', True)
book4 = Book(104, 'Paddoja', 'Ilma Behroj', True)
book5 = Book(105, 'Padmir', 'Ilma Behroj', True)
book6 = Book(106, 'Suicide Note', 'Md. Sahidul Islam Rajon', True)
book7 = Book(107, 'Asman', 'Lotiful Islam Sibly', True)
book8 = Book(108, 'Ontim', 'Lotiful Islam Sibly', True)

Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)
Library.entry_book(book5)
Library.entry_book(book6)
Library.entry_book(book7)
Library.entry_book(book8)

menu()
