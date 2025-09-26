 Breakdown of the Contact Book Code

### 1. **Importing modules**

```python
import json
import os
```

* `json` → to save & load contacts in a file (`contacts.json`).
* `os` → to check if the file already exists before loading.

### 2. **Loading & Saving Contacts**

```python
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []
```

* If `contacts.json` exists, load it into Python as a list of dictionaries.
* If not, return an empty list.

```python
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
```

* Saves all contacts back to `contacts.json` after any change.
### 3. **CRUD Operations**

👉 CRUD = **Create, Read, Update, Delete**

* **Create (Add Contact)**

```python
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!")
```

Adds a new contact (stored as a dictionary inside a list).

---

* **Read (View Contacts)**

```python
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
```

Displays all saved contacts

* **Search Contact**

```python
def search_contact(contacts):
    search_name = input("Enter name to search: ").lower()
    results = [c for c in contacts if search_name in c['name'].lower()]
    ...

Looks for a name in the contact list (case-insensitive).

* **Delete Contact**

```python
def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()
    updated_contacts = [c for c in contacts if c['name'].lower() != name]
    ...

Removes a contact by name and updates the JSON file.

### 4. **Main Menu (Loop)**

python
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

Keeps showing options until the user chooses **Exit**.

### 5. **Program Flow**

* Program starts → loads saved contacts.
* Shows menu → user selects option (1–5).
* Performs operation (CRUD).
* Saves changes in JSON file → so contacts stay even after closing the program.


