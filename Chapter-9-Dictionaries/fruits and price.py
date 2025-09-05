# Asks for three fruits and their prices, then prints them using a dictionary

fruits = {}  # create an empty dictionary

for i in range(3): # loop to input fruit names and prices
    fruit = input("Enter fruit name " + str(i + 1) + ": ")  # input fruit name
    price = float(input("Enter price of " + fruit + ": "))  # input fruit price

    fruits[fruit] = price  # add fruit name and price to dictionary

print("\nFruits and their prices are:")
for fruit, price in fruits.items():
    print(f"{fruit} : ${price} ")  # print fruit name and price 