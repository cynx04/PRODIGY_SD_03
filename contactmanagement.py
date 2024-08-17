import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Current Phone: {contacts[name]['phone']}, Current Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")


def search_contacts(contacts):
    """Search for a contact by name."""
    search_term = input("Enter the name or partial name to search: ").lower()
    results = {name: info for name, info in contacts.items() if search_term in name.lower()}

    if results:
        print("\nSearch Results:")
        for name, info in results.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found matching the search term.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice(1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
