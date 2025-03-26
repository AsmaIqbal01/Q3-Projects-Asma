import json

class BookCollection:
    """A Class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up the file storage."""
        self.book_list = []  # List to hold the collection of books
        self.storage_file = "books_data.json"  # File to store book data
        self.read_from_file()  # Load existing books from the file

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)  # Load books from JSON file
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []  # Start with an empty list if file not found or corrupted

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)  # Save the book list as JSON

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        # Gather book details from user input
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        # Create a new book dictionary
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }
        self.book_list.append(new_book)  # Add the new book to the collection
        self.save_to_file()  # Save the updated collection to file
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        # Search for the book by title
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)  # Remove the book from the list
                self.save_to_file()  # Save the updated collection to file
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")  # Inform the user if the book was not found

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by: \n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()  # Get search term from user
        # Find books matching the search term in title or author
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        # Display matching books
        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("No matching books found.\n")  # Inform the user if no books were found

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        # Search for the book by title
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                # Gather new details from user input, keeping existing values if left blank
                new_title = input(f"New title (current: {book['title']}): ") or book['title']
                new_author = input(f"New author (current: {book['author']}): ") or book['author']
                new_year = input(f"New publication year (current: {book['year']}): ") or book['year']
                new_genre = input(f"New genre (current: {book['genre ']}): ") or book['genre']
                new_read = input(f"Have you read this book? (yes/no, current: {'yes' if book['read'] else 'no'}): ").strip().lower()
                new_read = new_read == "yes" if new_read in ["yes", "no"] else book['read']

                # Update book details
                book.update({
                    "title": new_title,
                    "author": new_author,
                    "year": new_year,
                    "genre": new_genre,
                    "read": new_read,
                })
                self.save_to_file()  # Save the updated collection to file
                print("Book details updated successfully!\n")
                return
        print("Book not found!\n")  # Inform the user if the book was not found

    def show_all_books(self):
        """Display all books in the collection."""
        if not self.book_list:
            print("No books in the collection.\n")  # Inform the user if the collection is empty
        else:
            print("Your Book Collection:")
            for index, book in enumerate(self.book_list, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
            print()

    def show_reading_progress(self):
        """Display the reading progress of the books in the collection."""
        total_books = len(self.book_list)  # Get the total number of books
        if total_books == 0:
            print("No books in the collection to track progress.\n")  # Inform if there are no books
            return

        read_books = sum(1 for book in self.book_list if book["read"])  # Count read books
        print(f"You have read {read_books} out of {total_books} books.")
        print(f"Reading Progress: {read_books / total_books * 100:.2f}%\n")  # Display progress percentage

    def start_application(self):
        """Run the application loop with a user-friendly interface."""
        while True:
            print("🔰 Welcome to your Book Collection Manager! 🔰")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            # Handle user choices
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()  # Save before exiting
                print("Thank you for using Book Collection Manager, Good Bye!!!")
                break
            else:
                print("Invalid choice. Please try again.\n")  # Inform the user of invalid input


if __name__ == "__main__":
    book_manager = BookCollection()  # Create an instance of BookCollection
    book_manager.start_application()  # Start the application loop