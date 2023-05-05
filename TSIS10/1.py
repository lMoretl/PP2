import psycopg2
import csv

contacts = []


def display_contacts_list():
    if len(contacts) > 0:
        with open('output.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(contacts)

        print('Contacts: ')

        for c in contacts:
            print(f'{c[0]}. {c[1]} {c[2]}, {c[3]}')

        print('-' * 100)
        print('You can also see list of contacts in output.csv file')
    else:
        print('Contacts not found!')


def list_contacts():
    global contacts
    sql = 'select * from contacts order by id asc'

    cursor.execute(sql)
    contacts = cursor.fetchall()

    display_contacts_list()


connection = psycopg2.connect(
    host="localhost",
    database="pp2",
    user="postgres",
    password="FynjifPlayMoret"
)

cursor = connection.cursor()
choice = None


def find_contact_by_id(id: int):
    global contacts

    for contact in contacts:
        if contact[0] == id:
            return contact


while True:
    choice = input('PRESS [1] TO LIST ALL CONTACTS\n'
                   'PRESS [2] TO IMPORT CONTACTS FROM input.csv\n'
                   'PRESS [3] TO ADD NEW CONTACT GETTING DATA FROM CONSOLE\n'
                   'PRESS [4] TO UPDATE CONTACT INFO\n'
                   'PRESS [5] TO SEARCH CONTACT\n'
                   'PRESS [6] TO DELETE CONTACT\n'
                   'PRESS [0] TO EXIT\n')

    if choice == '1':
        list_contacts()

    elif choice == '2':

        with open('input.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            counter = 0
            for row in reader:
                counter += 1
                cursor.execute(f"""INSERT INTO contacts(name,surname,phone_number)
                VALUES ('{row[0]}','{row[1]}','{row[2]}')""")


        connection.commit()

        print(f'{counter} contacts have successfully been saved!')

    elif choice == '3':
        name = input('Insert name: ')
        surname = input('Insert surname: ')
        phone_number = input('Insert phone number: ')

        sql = f'insert into contacts (name, surname, phone_number) values (\'{name}\', \'{surname}\', \'{phone_number}\');'

        cursor.execute(sql)
        connection.commit()

        print('Contact has successfully be saved!')

    elif choice == '4':
        list_contacts()

        id = int(input('Write id of contact which you you to change: '))
        chosen_contact = find_contact_by_id(id)
        name = chosen_contact[1]
        surname = chosen_contact[2]
        phone_number = chosen_contact[3]

        if input('Do you want to change name? [y/n]\n') == 'y':
            name = input('Enter new name: ')
        if input('Do you want to change surname? [y/n]\n') == 'y':
            surname = input('Enter new surname: ')

        if input('Do you want to change phone number? [y/n]\n') == 'y':
            phone_number = input('Enter new phone number: ')

        sql = f'update contacts set name=\'{name}\', surname=\'{surname}\', phone_number=\'{phone_number}\' where id={id}'
        cursor.execute(sql)
        connection.commit()
        print('Contact info has successfully been updated!')

    elif choice == '5':
        choice_1 = input('PRESS [1] TO SEARCH CONTACT BY NAME\n'
                         'PRESS [2] TO SEARCH CONTACT BY SURNAME\n')

        part_of_statement = f'{"sur" if choice_1 == "2" else ""}name'

        parameter = input(f'Insert {part_of_statement}: ')

        sql = f'select * from contacts where {part_of_statement}=\'{parameter}\''

        cursor.execute(sql)
        contacts = cursor.fetchall()

        display_contacts_list()

    elif choice == '6':
        choice_1 = input('PRESS [1] TO SEARCH CONTACT BY NAME\n'
                         'PRESS [2] TO SEARCH CONTACT BY SURNAME\n'
                         'PRESS [3] TO SEARCH CONTACT BY PHONE NUMBER\n')

        part_of_statement = "phone_number" if choice_1 == "3" else "surname" if choice_1 == "2" else "name"
        parameter = input(f'Insert {part_of_statement}: ')

        sql = f'select * from contacts where {part_of_statement}=\'{parameter}\''

        cursor.execute(sql)
        contacts = cursor.fetchall()

        id = None

        if len(contacts) == 0:
            print('Contact not found!')
        else:
            if len(contacts) > 1:
                display_contacts_list()
                id = int(input(f'Insert the id of contact which you are planning to delete: '))

            else:
                if input(f'Are you sure to delete {contacts[0][1]} {contacts[0][1]}?[y/n]') == 'y':
                    id = contacts[0][0]
            sql = f'delete from contacts where id={id}'
            cursor.execute(sql)
            connection.commit()
            print('Contact has successfully been deleted!')


    elif choice == '0':
        break

    print('=' * 120)

# cursor.execute(sql_request)

# contacts = cursor.fetchall()

# print(contacts)

cursor.close()
connection.close()