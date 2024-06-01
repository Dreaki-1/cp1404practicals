for i in range(1, 21, 2):
    print(i, end=' ')
print()


# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()


# b.
for i in range(21, 0, -1):
    print(i, end=' ')
print()

# c:
quantity_of_stars = int(input('Enter number of stars: '))
for i in range(quantity_of_stars):
    print('*', end="")

# d.
quantity_of_stars = int(input('Enter number of stars: '))
for i in range(1, quantity_of_stars + 1):
    print('*' * i)
