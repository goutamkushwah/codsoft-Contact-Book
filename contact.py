class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Name\t\tPhone\t\tEmail\t\tAddress")
            for contact in self.contacts:
                print(f"{contact.name}\t{contact.phone}\t{contact.email}\t{contact.address}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"{contact.name} updated successfully.")
                break
        else:
            print(f"{name} not found in contacts.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"{contact.name} deleted successfully.")
                break
        else:
            print(f"{name} not found in contacts.")

def save_contacts_to_file(contacts):
    with open('contacts.txt', 'w') as f:
        for contact in contacts:
            f.write(f"{contact.name},{contact.phone},{contact.email},{contact.address}\n")

def load_contacts_from_file():
    contacts = []
    try:
        with open('contacts.txt', 'r') as f:
            for line in f:
                name, phone, email, address = line.strip().split(',')
                contacts.append(Contact(name, phone, email, address))
    except FileNotFoundError:
        print("No existing contacts found. Starting with an empty contact list.")
    return contacts

def main():
    contact_book = ContactBook()

    # Load existing contacts from file (if any)
    contact_book.contacts = load_contacts_from_file()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            email = input("Enter the contact email: ")
            address = input("Enter the contact address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print(f"{name} added to contacts.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter a name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"{contact.name} ({contact.phone})")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the contact name to update: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            save_contacts_to_file(contact_book.contacts)
            print("Contacts saved to file. Exiting the contact management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
