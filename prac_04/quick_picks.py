import random

LOW = 1
HIGH = 45
NUMBER_PER_LINE = 6


def main():
    """Programs that selects random numbers from 1 to 45 in lines of 6"""
    pick = int(input("How many picks? "))
    while pick < 0:
        print("invalid input must be more then 0")
        pick = int(input("How many picks? "))
    for i in range(pick):
        picks = []
        for j in range(NUMBER_PER_LINE):
             number = random.randint(LOW, HIGH)
             while number in picks:
                 number = random.randint(LOW, HIGH)
             picks.append(number)
        picks.sort()
        print(" ".join(f"{number:2}" for number in picks))

main()