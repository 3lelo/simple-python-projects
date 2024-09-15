# Managing Library Books

def is_empty(type : str , name : str) -> bool:
    '''Check if the user ignored the input.'''
    if not name:
        print (f"\nYou shouldn't leave the {type} empty!")
        return True
    return False


def display_choices() -> None:
    print('''
Library Menu:
1. Add a book
2. Display books
3. Search for a book
4. Delete a book
5. Update book data
6. Exit''')

# Start program
from LibraryModule import LMS
inventory = LMS()

# Loop to display the choices and processes user input until the user choice to exit
def main() -> None:
    running = True
    while running:
        display_choices()

        choice = input("Select an option (1-6) : ").strip()
        match choice:
            case '6':
                print ("\nThanks for using our library system. Goodbye!")
                running = False

            case '1':
                title = input("Enter the book title : ").strip()
                if is_empty('Title' , title):
                    continue

                author = input("Enter the book author : ").strip()
                if is_empty("Author" , author):
                    continue

                inventory.add_book(title , author)

            case '2':
                inventory.display_books()

            case '3':
                title = input("Enter the title of the book to search : ").strip()
                if is_empty("Title" , title):
                    continue

                inventory.search_book(title)

            case '4':
                title = input("Enter the title of the book to delete : ").strip()
                if is_empty("Title" , title):
                    continue

                inventory.delete_book(title)

            case '5':
                title = input("Enter the title of the book to update : ").strip()
                if is_empty("Title" , title):
                    continue

                inventory.update_book(title)

            case _:
                print ("\nInvalid choice!")

if __name__ == "__main__":
    main()