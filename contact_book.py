from add_books import Add_Contact_Book
from save_all_book import save_contact_book
from view_all_book import View_all_books
from search_book import search
from remove_book import remove

all_contact_books = []

while True:
    print('0. Exit')
    print('1. Add Contact Book')
    print('2. Save All Book')
    print('3. View All Book')
    print('4. Search Contact Book')
    print('5. Remove Contact Book')

    menu = int(input('Choose any number'))

    if menu == 0:
        print('Thanks for using Contact Book Management System')
        break
    elif menu == 1:
        Add_Contact_Book(all_contact_books)
    elif menu == 2:
        save_contact_book(all_contact_books)
    elif menu == 3:
        View_all_books(all_contact_books)
    elif menu == 4:
        search(all_contact_books)
    elif menu == 5:
        remove(all_contact_books)
    else:
        print('Your Menu Number is Wrong!')

