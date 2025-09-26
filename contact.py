import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file (if exists)
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(" Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search contact by name
def search_contact(contacts):
    search_name = input("Enter name to search: ").lower()
    results = [c for c in contacts if search_name in c['name'].lower()]

    if results:
        for contact in results:
            print(f" Found: {contact['name']} | {contact['phone']} | {contact['email']}")
    else:
        print(" Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()
    updated_contacts = [c for c in contacts if c['name'].lower() != name]

    if len(updated_contacts) < len(contacts):
        save_contacts(updated_contacts)
        print("🗑 Contact deleted successfully!")
        return updated_contacts
    else:
        print(" Contact not found.")
        return contacts

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            contacts = delete_contact(contacts)
        elif choice == "5":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Try again!")

if __name__ == "__main__":
    main()
