import json # Import JSON module to handle file storage
#json is used to store and retrieve data from the JSON file.
import os   # Import OS module to check file existence
#os is used to check if the file exists before reading from it.


# File to store library data
data_file = 'library.txt' 

def load_library():
    if os.path.exists(data_file):
        # Check if file exists before reading from it
        try:
            with open(data_file, 'r') as file:
                return json.load(file) # Load JSON data from file
        except json.JSONDecodeError: # Handle JSON decoding error
            print('Error reading from file. Creating new library.')
            return []
    return []
# If library.txt exists, it loads the books stored inside.
# If the file is empty or corrupted, it returns an empty list.

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4) # Save library data to file in JSON format

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes' # Convert input to Boolean
    
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book) # Add new book to list
    save_library(library) # Save updated list to file
    print(f'Book {title} added successfully!')

    # Removed the return statement as it is not needed
def remove_book(library):
    title = input("Enter the title of the book you'd like to remove from library: ")
    initial_length = len(library) # Store initial number of books
    # Create a new list excluding the book to be removed
    library[:] = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length: # If a book was removed
        save_library(library) # Save updated list to file
        print(f'Book {title} removed successfully!')
    else:
        print(f'Book {title} not found in library!')

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    if search_by not in ['title', 'author']: # Validate input
        print('Invalid search criteria. Please try again!')
        return
    
    search_term = input (f"Enter the {search_by}: ").lower()
    # Search books where the search term appears in the title or author

    results =[book for book in library if search_term in book[search_by].lower()]
    if results:
        for book in results:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print(f"No books found with {search_by} '{search_term}'")

def display_all_books(library):
    if library: # Check if library is not empty
        for book in library:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print('No books in library yet!')

def display_statistics(library):
    total_books = len(library) # Get total number of books
    read_books = len([book for book in library if book['read']]) # Get number of read books
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0 # Calculate percentage read books
    print(f'Total books: {total_books}')
    print(f'Percentage read: {percentage_read:.2f}%')

def main():
    library = load_library() # Load library data on start
    while True:
        print("\nWelcome to your personal Library Manager!")
        print("Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again!')

if __name__ == '__main__':
    main()

