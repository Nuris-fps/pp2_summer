import csv
from connect import connect
from config import load_config


config = load_config()
conn = connect(config)
cur = conn.cursor()


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        """
        INSERT INTO contacts (first_name, phone)
        VALUES (%s, %s)
        """,
        (name, phone)
    )

    conn.commit()
    print("Contact added.")


def insert_from_csv():
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) < 2:
                continue

            cur.execute(
                """
                INSERT INTO contacts (first_name, phone)
                VALUES (%s, %s)
                """,
                (row[0], row[1])
            )

    conn.commit()
    print("CSV contacts inserted.")


def update_contact():
    print("1 - Update name")
    print("2 - Update phone")

    choice = input("Choose option: ")

    if choice == "1":
        old_name = input("Enter current name: ")
        new_name = input("Enter new name: ")

        cur.execute(
            """
            UPDATE contacts
            SET first_name = %s
            WHERE first_name = %s
            """,
            (new_name, old_name)
        )

    elif choice == "2":
        name = input("Enter contact name: ")
        new_phone = input("Enter new phone: ")

        cur.execute(
            """
            UPDATE contacts
            SET phone = %s
            WHERE first_name = %s
            """,
            (new_phone, name)
        )

    conn.commit()
    print("Contact updated.")


def query_contacts():
    print("1 - Show all contacts")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose option: ")

    if choice == "1":
        cur.execute("SELECT * FROM contacts")

    elif choice == "2":
        name = input("Enter name: ")

        cur.execute(
            """
            SELECT * FROM contacts
            WHERE first_name ILIKE %s
            """,
            ('%' + name + '%',)
        )

    elif choice == "3":
        prefix = input("Enter phone prefix: ")

        cur.execute(
            """
            SELECT * FROM contacts
            WHERE phone LIKE %s
            """,
            (prefix + '%',)
        )

    rows = cur.fetchall()

    print("\nContacts:")

    for row in rows:
        print(row)


def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by phone")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")

        cur.execute(
            """
            DELETE FROM contacts
            WHERE first_name = %s
            """,
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")

        cur.execute(
            """
            DELETE FROM contacts
            WHERE phone = %s
            """,
            (phone,)
        )

    conn.commit()
    print("Contact deleted.")


while True:
    print("\nPHONEBOOK MENU")
    print("1 - Insert from console")
    print("2 - Insert from CSV")
    print("3 - Update contact")
    print("4 - Query contacts")
    print("5 - Delete contact")
    print("6 - Exit")

    option = input("Choose option: ")

    if option == "1":
        insert_from_console()

    elif option == "2":
        insert_from_csv()

    elif option == "3":
        update_contact()

    elif option == "4":
        query_contacts()

    elif option == "5":
        delete_contact()

    elif option == "6":
        break


cur.close()
conn.close()