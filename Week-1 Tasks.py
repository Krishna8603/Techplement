import json

# Function to save contacts
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Contacts saved successfully!")

# Function to load contacts
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to display the menu
def main_menu():
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. List All Contacts")
    print("5. Save & Exit")

# Function to add a contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    
    # Validate inputs
    if not name or not phone:
        print("Name and phone are required!")
        return
    
    # Append to contacts list
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to search a contact
def search_contact(contacts):
    name = input("Enter Name to Search: ").strip()
    results = [c for c in contacts if c['name'].lower() == name.lower()]
    
    if results:
        for contact in results:
            print(contact)
    else:
        print("No contact found with that name.")

# Function to update a contact
def update_contact(contacts):
    name = input("Enter Name to Update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found: {contact}")
            contact['phone'] = input("Enter New Phone Number: ").strip() or contact['phone']
            contact['email'] = input("Enter New Email: ").strip() or contact['email']
            print("Contact updated successfully!")
            return
    print("No contact found with that name.")

# Function to list all contacts
def list_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for contact in contacts:
        print(contact)

# Main program loop
def main():
    contacts = load_contacts()  # Ensure this function is defined above
    while True:
        main_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "5":
            save_contacts(contacts)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
