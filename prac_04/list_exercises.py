<<<<<<< HEAD
"""
List Exercises
CP1404
"""


# Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")





# Woefully inadequate secuirty checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input('Enter username:')
if username in usernames:
    print("Acess Granted")
else:
    print("Access Denied")

=======
"""
List Exercises
CP1404
"""


# Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")





# Woefully inadequate secuirty checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input('Enter username:')
if username in usernames:
    print("Acess Granted")
else:
    print("Access Denied")

>>>>>>> origin/master
