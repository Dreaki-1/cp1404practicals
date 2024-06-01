MENU = "(H)ello\n(G)oodbye\n(Q)uit"

user_name = input("Enter name: ")
print(MENU)
choice = input("Enter choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")
    elif choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid Choice")
    print(MENU)
    choice = input("Enter choice: ").upper()
if choice == "Q":
    print("Finished.")