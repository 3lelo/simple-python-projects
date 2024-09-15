def is_book_in_library(title : str , books : list) -> bool:
    '''Check if the book's entered title is in the library'''
    return True if any(book['title'] == title for book in books) else False

class LMS:
    '''A class to manage books in the library like adding, displaying, searching, updating and deleting books'''
    def __init__(self):
        self.books = [] # Initialize an empty list to store books in the library.
    

    def add_book(self, title : str , author : str) -> None:
        '''Allows the user to add a new book to the library or display a message if the book already exists.'''
        if is_book_in_library(title , self.books):
            print (f"\nBook with title: {title}, already exists in the library!")
        
        else:
            book = {'title' : title , 'author': author}
            self.books.append(book)
            print ("\nBook added successfully.")


    def display_books(self) -> None:
        '''Display the all books currently in the library or a message if the library is empty'''
        if not self.books:
            print ("\nThe library is empty!")

        else:
            print ("\nLibrary books:")
            for book in self.books:
                print(f"Title : {book['title']} , Author : {book['author']}")
        

    def search_book(self, title : str) -> None:
        '''Search for a book by its title and display its details or a message if the book not found.'''
        if is_book_in_library(title , self.books):
            book = next(book for book in self.books if book['title'] == title)

            print (f"\nTitle : {title} , Author : {book['author']}")
            
        else:
            print ("\nBook not found in the library!")


    def delete_book(self, title : str) -> None:
        '''Delete a book by its title or display a message if the book not found.'''
        if is_book_in_library(title , self.books):
            self.books = [book for book in self.books if book['title'] != title]
            print ("\nBook deleted successfully.")
            
        else:
            print ("\nBook not found in the library!")


    def update_book(self, title : str) -> None:
        '''Update a book's details by its title or display a message if the book not found.'''
        if is_book_in_library(title , self.books):
            book = next(book for book in self.books if book['title'] == title)

            new_title = input("Enter the new title (or press Enter to keep current title) : ").strip()
            if is_book_in_library(new_title , self.books):
                print ("\nBook with this title already exists in the library!\n")

            else:
                book['title'] = new_title if new_title else title

            new_author = input("Enter the new author (or press Enter to keep current author) : ").strip()
            book['author'] = new_author if new_author else book['author']

            print ("\nBook updated successfully.")
            
        else:
            print ("\nBook not found in the library!")
