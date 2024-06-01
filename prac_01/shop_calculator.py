
DISCOUNT = 0.1
price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price += float(input("Price of item: "))
if price > 100:
    total_price = price - (price * DISCOUNT)
else:
    total_price = price
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
