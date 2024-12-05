from save_all_book import save_contact_book
# from contact_book import all_contact_books
def Add_Contact_Book(all_contact_books):
    Name = input('Enter Your Name: ')
    Email = input('Enter Your Emial: ')
    Phone_Number = int(input('Enter Your Phone Number: '))
    Address = input('Enter Your Address: ')


    Contact_book = {
        'Name':Name,
        'Email':Email,
        'Phone_Number':Phone_Number,
        'Address':Address,
    }
    pnl = []
    for i in all_contact_books:
        # v=list(i.values())
        pn = (i['Phone_Number'])
        pnl.append(pn)
        # print(v,Phone_Number)
    
    if Phone_Number not in pnl:
        all_contact_books.append(Contact_book)
        save_contact_book(all_contact_books)
        print('Added Successfully.')
        return Contact_book