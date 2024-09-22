contacts = [] 
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter physical address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("\nContact added successfully!\n")
def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
        print()
def search_contact():
    query = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("\nNo contacts found with the given query.\n")
def update_contact():
    view_contacts()  
    index = int(input("Enter the contact number to update: ")) - 1
    if 0 <= index < len(contacts):
        print("\nEnter new details (press Enter to keep current value):")
        new_name = input(f"Name [{contacts[index]['name']}]: ") or contacts[index]['name']
        new_phone = input(f"Phone [{contacts[index]['phone']}]: ") or contacts[index]['phone']
        new_email = input(f"Email [{contacts[index]['email']}]: ") or contacts[index]['email']
        new_address = input(f"Address [{contacts[index]['address']}]: ") or contacts[index]['address']
        contacts[index] = {
            'name': new_name,
            'phone': new_phone,
            'email': new_email,
            'address': new_address
        }
        print("\nContact updated successfully!\n")
    else:
        print("\nInvalid contact number.\n")
def delete_contact():
    view_contacts()  
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"\nContact '{deleted_contact['name']}' deleted successfully!\n")
    else:
        print("\nInvalid contact number.\n")
def contact_manager():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.\n")
contact_manager()