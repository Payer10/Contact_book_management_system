def save_contact_book(all_contact_books):
    with open('all_contact_books.csv','w') as fp:
        for books in all_contact_books:
            output = f'{books['Name']} , {books['Email']} , {books['Phone_Number']} , {books['Address']}'
            fp.write(output)