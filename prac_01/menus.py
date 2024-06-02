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


    def determine_score_status(score):
        """Take user's score and determine the status"""
        if score < 0 or score > 100:
            return "Invalid score"
        elif score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"