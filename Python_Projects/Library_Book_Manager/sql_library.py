# Import MySQL connector module to interact with the database
import mysql.connector


#  Establish MySQL Connection

conn = mysql.connector.connect(
    host = 'localhost',
    user="sql_library",  # Change to your MySQL username
    password="Karachi1",  # Change to your MySQL password
    database="library_manager"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,  # Unique ID for each book
    title VARCHAR(255) NOT NULL, # Title of the book
    author VARCHAR(255) NOT NULL, # Author of the book
    year INT NOT NULL, # Year of publication
    genre VARCHAR(100), # Genre of the book
    read_status BOOLEAN NOT NULL  # Read status (TRUE = Read, FALSE = Unread)
)
               
""")
conn.commit() # Commit the table creation to the database


def add_book():
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'
    
   # SQL Query to insert book details into the database
    query = "INSERT INTO books (title, author, year, genre, read_status) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author, year, genre, read)
    cursor.execute(query, values) # Execute query
    conn.commit() # Save changes to the database
 
    print(f'Book {title} added successfully!')

    # Removed the return statement as it is not needed
def remove_book():
    title = input("Enter the title of the book you'd like to remove from library: ")
    # SQL Query to delete a book where the title matches
    query = "DELETE FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    conn.commit() # Save changes to the database
     # Check if the book was found and deleted
    if cursor.rowcount > 0:
        print(f'Book {title} removed successfully!')
    else:
        print(f'Book {title} not found in library!')

def search_library():
    search_by = input("Search by title or author: ").lower()
    # Validate input (Only accept 'title' or 'author')
    if search_by not in ['title', 'author']:
        print('Invalid search criteria. Please enter "title" or "author".')
        return

    search_term = input(f"Enter the {search_by}: ").lower() # Get search term 
    query = f"SELECT title, author, year, genre, read_status FROM books WHERE {search_by} LIKE %s"
    
    cursor.execute(query, ('%' + search_term + '%',)) # Execute query with wildcard search
    results = cursor.fetchall() # Fetch all matching books

    # Display results
    if results:
        for book in results:
            status = "Read" if book[4] else "Unread"
            print(f"{book[0]} by {book[1]} ({book[2]}) - {book[3]} - {status}")
    else:
        print(f"No books found with {search_by} '{search_term}'")


def display_all_books():
    cursor.execute("SELECT title, author, year, genre, read_status FROM books")  # Fetch all books
    books = cursor.fetchall()

    if books:
        for book in books:
            status = "Read" if book[4] else "Unread"
            print(f"{book[0]} by {book[1]} ({book[2]}) - {book[3]} - {status}")
    else:
        print("No books in the library yet!")


def display_statistics():
    cursor.execute("SELECT COUNT(*) FROM books") # Get total books count
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = TRUE") # Count read books
    read_books = cursor.fetchone()[0]

    # Calculate the percentage of read books
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    # Print statistics
    print(f'Total books: {total_books}')
    print(f'Percentage read: {percentage_read:.2f}%')


def main():
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
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_library()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            print('Goodbye!')
            conn.close()  # Close MySQL connection before exiting
            break
        else:
            print('Invalid choice. Please try again!')

if __name__ == '__main__':
    main()

