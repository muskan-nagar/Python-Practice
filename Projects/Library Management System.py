#WEEK 2 MINI PROJECT
#Library Management System
library=[]
def add_book():
    Book_name=input("Enter name of book:")
    Book_ID=int(input("Enter id of book:"))
    Author=input("Enter author of book:")
    Quantity=int(input("Enter quantity of book:"))
    Book={"ID":Book_ID,"Name":Book_name,"Author":Author,"Quantity":Quantity}
    library.append(Book)
    print("Book added succesfully.\n")
def remove_book():
    value=int(input("Enter  name or Id of book:"))
    for book in library:
        if str(book["ID"]) == value or book["Name"].lower()==value.lower():
            library.remove(book)
            print("Book removed!\n")
            return
    print("Book not found!\n")

def search_book():
    BOOK=input("Enter name or Id of book:")
    for Book in library:
        if Book["Name"].lower() ==BOOK.lower() or str(Book["ID"]== BOOK):
            print("Book Found!\n")
            print(Book)
            return
    print("Book not found!\n")

def display_book():
    if not library:
        print("No books available.\n")
    else:
        print("\n-----Library-----\n")
        for books in library:
            print(books)

def save_books():
    with open("library.txt","w") as file:
        for book in library:
            file.write(str(book)+ "\n")  
    print("Books saved successfully.\n")

def load_books():
    try:
        with open("library.txt") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("No saved books found.\n")

def Library():
    while True:
        print("1.Add book\n2.Remove book\n3.Search book\n4.Display all books\n5.Save books\n6.Load books\n7.Exit\n")
        choice=input("Enter your choice:")

        if choice =="1":
            add_book()
        elif choice =="2":
            remove_book()
        elif choice =="3":
            search_book()
        elif choice =="4":
            display_book()
        elif choice =="5":
            save_books()
        elif choice =="6":
            load_books()
        elif choice=="7":
            print("Thanks for joining. Goodbye!")
            break
        else:
            print("Invalid. Choose from above mentioned options.\n")
Library()