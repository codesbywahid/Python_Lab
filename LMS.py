books = []
members = []
next_book_id = 1

def add_book():
    global next_book_id

    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    genre = input("Enter Genre of Book: ")

    book = {
        "book_id": next_book_id,
        "title": title,
        "author": author,
        "genre": genre,
        "available": True
    }

    books.append(book)
    next_book_id += 1

    print("Book added successfully!")


def view_books():
    if not books:
        print("No books found.")
        return

    print("\n========== ALL BOOKS ==========")

    for book in books:
        print("\nBook ID:", book["book_id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Genre:", book["genre"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Borrowed")


def find_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book

    return None


def delete_book():
    choice = input("Enter Book Title: ")
    book = find_book(choice)

    if book is None:
        print("Book not found.")
    elif not book["available"]:
        print("Book is currently borrowed and cannot be deleted.")
    else:
        books.remove(book)
        print("Book deleted successfully.")


def search_books():
    choice = input("Enter book title or author: ").lower()

    found = False

    for book in books:
        if (choice in book["title"].lower() or
                choice in book["author"].lower()):

            found = True

            print("\nBook ID:", book["book_id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Genre:", book["genre"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Borrowed")

    if not found:
        print("No matching books found.")


def show_genres():
    if not books:
        print("No books available.")
        return

    genres = set()

    for book in books:
        genres.add(book["genre"])

    print("\nGenres:")

    for genre in genres:
        print("-", genre)

def add_member():
    name = input("Enter Member Name: ")
    if find_member(name) is not None:
        print("Member already exists.")
        return

    member = {
        "member": name,
        "borrowed books": []
    }

    members.append(member)

    print("Member added successfully!")


def view_members():
    if not members:
        print("No members found.")
        return

    print("\n========== ALL MEMBERS ==========")

    for member in members:
        print("\nMember:", member["member"])
        print("Borrowed Books:", len(member["borrowed books"]))

        if member["borrowed books"]:
            print("Books:")

            for book in member["borrowed books"]:
                print("-", book)


def find_member(name):
    for member in members:
        if name.lower() == member["member"].lower():
            return member

    return None


def delete_member():
    choice = input("Enter Member Name: ")
    member = find_member(choice)

    if member is None:
        print("Member not found.")

    elif len(member["borrowed books"]) > 0:
        print("Cannot delete member.")
        print("This member still has borrowed books.")

    else:
        members.remove(member)
        print("Member deleted successfully.")

def borrow_book():
    choice = input("Enter Member Name: ")
    member = find_member(choice)

    if member is None:
        print("Member not found.")
        return

    b_choice = input("Enter Book Title: ")
    book = find_book(b_choice)

    if book is None:
        print("Book not found.")

    elif not book["available"]:
        print("Book is already borrowed.")

    else:
        member["borrowed books"].append(book["title"])
        book["available"] = False

        print("Book borrowed successfully!")


def return_book():
    choice = input("Enter Member Name: ")
    member = find_member(choice)

    if member is None:
        print("Member not found.")
        return

    b_choice = input("Enter Book Title: ")

    borrowed_book = None

    for title in member["borrowed books"]:
        if title.lower() == b_choice.lower():
            borrowed_book = title
            break

    if borrowed_book is None:
        print("This member hasn't borrowed that book.")
        return

    book = find_book(borrowed_book)

    if book is not None:
        book["available"] = True

    member["borrowed books"].remove(borrowed_book)

    print("Book returned successfully!")
def main_menu():
    while True:
        print("\n================================")
        print("       LIBRARY MANAGEMENT")
        print("================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Show Genres")
        print("6. Add Member")
        print("7. View Members")
        print("8. Delete Member")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            show_genres()
        elif choice == "6":
            add_member()
        elif choice == "7":
            view_members()
        elif choice == "8":
            delete_member()
        elif choice == "9":
            borrow_book()
        elif choice == "10":
            return_book()
        elif choice == "11":
            print("Exiting Library Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()