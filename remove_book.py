def remove(contact_all_books):
    v = input('Enter your name: ')
    for i in contact_all_books:
        if v == i['Name']:
            del i
            print('Your dictionry removed')
            break