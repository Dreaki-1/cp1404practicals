
"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from docutils.transforms import parts

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def display_subject_details(data):
    for content in data:
        subject = content[0]
        teacher = content[1]
        capacity = content[2]
        print(f"{subject} is taught by {teacher} and has {capacity} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts = []
    for line in input_file:
        line = line.strip()
        line = line.split(",")
        parts.append(line)
    input_file.close()
    return parts


main()

"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from docutils.transforms import parts

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def display_subject_details(data):
    for content in data:
        subject = content[0]
        teacher = content[1]
        capacity = content[2]
        print(f"{subject} is taught by {teacher} and has {capacity} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts = []
    for line in input_file:
        line = line.strip()
        line = line.split(",")
        parts.append(line)
    input_file.close()
    return parts


main()

