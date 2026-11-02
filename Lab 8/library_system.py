# Library Record System


def add_book(books):
    isbn = input("Book ID / ISBN: ")
    copies = int(input("Number of copies to add: "))
    if isbn in books:
        books[isbn]["copies"] += copies
        print("Copies added.")
    else:
        title = input("Title: ")
        author = input("Author: ")
        books[isbn] = {"title": title, "author": author, "copies": copies, "issued_to": []}
        print("Book added.")


def issue_book(books):
    isbn = input("Book ID / ISBN: ")
    member = input("Member ID: ")
    if isbn not in books:
        print("Book not found.")
        return
    held = 0
    for book in books.values():
        if member in book["issued_to"]:
            held += 1
    if member in books[isbn]["issued_to"]:
        print("This member already has this book.")
    elif held >= 2:
        print("A member can hold at most two books.")
    elif books[isbn]["copies"] == 0:
        print("No copies are available.")
    else:
        books[isbn]["copies"] -= 1
        books[isbn]["issued_to"].append(member)
        print("Book issued.")


def return_book(books):
    isbn = input("Book ID / ISBN: ")
    member = input("Member ID: ")
    if isbn in books and member in books[isbn]["issued_to"]:
        books[isbn]["issued_to"].remove(member)
        books[isbn]["copies"] += 1
        print("Book returned.")
    else:
        print("That member does not have this book.")


def show_reports(books):
    author = input("Author to search for: ").lower()
    print("Books by", author + ":")
    for book_id, book in books.items():
        if book["author"].lower() == author:
            print(book_id, book["title"])

    member_books = {}
    for book_id, book in books.items():
        for member in book["issued_to"]:
            if member not in member_books:
                member_books[member] = []
            member_books[member].append(book_id)
    print("Members holding more than one book:")
    for member, titles in member_books.items():
        if len(titles) > 1:
            print(member, titles)
    print("Unavailable:", [book_id for book_id, book in books.items() if book["copies"] == 0])
    print("Never issued:", [book_id for book_id, book in books.items() if not book["issued_to"]])


def main():
    books = {}
    while True:
        print("\nLIBRARY MENU: 1 Add book  2 Issue  3 Return  4 Search  5 Reports  6 Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            issue_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            isbn = input("Book ID / ISBN: ")
            print(books.get(isbn, "Book not found."))
        elif choice == "5":
            show_reports(books)
        elif choice == "6":
            break
        else:
            print("Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
