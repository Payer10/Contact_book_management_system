def View_all_books(all_contact_books):
    if all_contact_books != []:
        for books in all_contact_books:
            print(f'Name: {books['Name']} | Email: {books['Email']} | Phone_Number: {books['Phone_Number']} | Address: {books['Address']}')