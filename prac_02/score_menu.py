"""
Practical_02 Score_Menu
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Must be between 0 and 100")
                choice = input("> ").upper()
        elif choice == "P":
            status = determine_score_status(score)
            print(status)
        elif choice == "S":
            star_score = convert_int_to_asterisk(score)
            print(star_score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input("> ").upper()


def convert_int_to_asterisk(score):
    star_score = '*' * score
    return star_score


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


main()
