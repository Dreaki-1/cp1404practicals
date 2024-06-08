"""Files Prac 03 """


"1."

with open("name.txt", "w") as out_file:
    name = input("Enter Name: ")
    print(name, file=out_file)

#Alternate Method

out_file = open("name.txt", "w")
name = input("Enter Name: ")
print(name, file=out_file)
out_file.close()


"2."

in_file = open("name.txt", "r")
lines = in_file.readlines()
in_file.close()
name = lines[0].strip()
print(f"Hi {name}!")


" 3."

with open("numbers.txt") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    in_file.close()
    print(f"{first_number} + {second_number} = {first_number+second_number}")

" 4. "

with open("numbers.txt") as in_file:
    total_lines = 0
    for line in in_file:
        number = int(line)
        total_lines += number
    print(total_lines)

