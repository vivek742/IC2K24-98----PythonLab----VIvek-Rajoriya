# Phone Directory


def number_is_valid(number):
    return len(number) == 10 and number.isdigit()


def find_number_owner(contacts, number):
    # Create a dictionary from phone number to contact name.
    number_to_name = {}
    for name, contact in contacts.items():
        for phone in contact["phones"]:
            number_to_name[phone] = name
    return number_to_name.get(number)


def add_contact(contacts):
    name = input("Name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("10-digit phone number: ")
    if not number_is_valid(phone):
        print("Enter exactly 10 digits.")
        return
    if find_number_owner(contacts, phone):
        print("That number already belongs to someone else.")
        return
    email = input("Email: ")
    city = input("City: ")
    contacts[name] = {"phones": [phone], "email": email, "city": city}
    print("Contact added.")


def search_contact(contacts):
    search = input("Enter part of a name: ").lower()
    found = False
    for name, contact in contacts.items():
        if search in name.lower():
            print(name, contact)
            found = True
    if not found:
        print("No matching contact.")


def show_reports(contacts):
    cities = {}
    for name, contact in contacts.items():
        city = contact["city"]
        if city not in cities:
            cities[city] = []
        cities[city].append(name)
    print("Contacts by city:", cities)

    print("Contacts with more than one number:")
    for name, contact in contacts.items():
        if len(contact["phones"]) > 1:
            print(name, contact["phones"])

    print("Phone directory:")
    for name in sorted(contacts):
        print(name, contacts[name]["phones"], contacts[name]["email"], contacts[name]["city"])

    phone = input("Number to look up (or press Enter to skip): ")
    if phone:
        owner = find_number_owner(contacts, phone)
        print("Number belongs to:", owner if owner else "nobody in the directory")


def main():
    contacts = {}
    while True:
        print("\nPHONE MENU: 1 Add contact  2 Add number  3 Update email/city")
        print("4 Delete contact  5 Search name  6 Reports  7 Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            name = input("Contact name: ")
            if name not in contacts:
                print("Contact not found.")
                continue
            phone = input("10-digit phone number: ")
            if not number_is_valid(phone):
                print("Enter exactly 10 digits.")
            elif find_number_owner(contacts, phone):
                print("That number already belongs to someone else.")
            else:
                contacts[name]["phones"].append(phone)
                print("Number added.")
        elif choice == "3":
            name = input("Contact name: ")
            if name not in contacts:
                print("Contact not found.")
                continue
            field = input("Enter email or city: ").lower()
            if field == "email" or field == "city":
                contacts[name][field] = input("New " + field + ": ")
                print("Updated.")
            else:
                print("Choose email or city.")
        elif choice == "4":
            name = input("Contact name: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            show_reports(contacts)
        elif choice == "7":
            break
        else:
            print("Choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
