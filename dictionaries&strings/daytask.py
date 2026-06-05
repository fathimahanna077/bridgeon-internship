# Contact Book

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("Type 'exit' to quit")

    choice = input("\nEnter your choice: ").lower()

    if choice == "exit":
        print("Exiting Contact Book...")
        break

    elif choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print(f"✅ Contact '{name}' added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")

        phone = contacts.get(name)

        if phone:
            print(f"📞 {name}: {phone}")
        else:
            print(f"❌ Contact '{name}' not found.")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            new_phone = input("Enter new phone number: ")

            contacts[name] = new_phone

            print(f"✅ Contact '{name}' updated.")
        else:
            print(f"❌ Contact '{name}' not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]

            print(f"✅ Contact '{name}' deleted.")
        else:
            print(f"❌ Contact '{name}' not found.")

    elif choice == "5":
        if not contacts:
            print("📭 No contacts available.")
        else:
            print("\n===== CONTACT LIST =====")

            for name in sorted(contacts):
                print(f"{name} : {contacts[name]}")

    else:
        print("❌ Invalid choice. Try again.")