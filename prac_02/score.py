"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif 50 <= score < 90:
    print("Passable")
elif score < 100:
    print("Excellent")



"""
CP1404/CP5632 - Practical 02
Broken program to determine score status
"""


def main():
    """Get a user input and display score status"""
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(status)


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
