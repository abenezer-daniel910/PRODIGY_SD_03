import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file, or return an empty dictionary if the file does not exist."""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading the contacts file. It may be corrupted.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading contacts: {e}")
            return {}
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    try:
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving contacts: {e}")

def add_contact(contacts):
    """Add a new contact to the contacts dictionary."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    if not name or not phone or not email:
        print("All fields are required.")
        return
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact you want to edit: ").strip()
    if name in contacts:
        print(f"Editing contact '{name}'. Leave field blank to keep current value.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")