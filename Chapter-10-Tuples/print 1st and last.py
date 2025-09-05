# Asks for 5 numbers and prints the 1st and last number using tuple

numbers = []  # create an empty list

for i in range(5): # loop to input 5 numbers
    num = float(input("Enter number " + str(i + 1) + ": "))  # input number
    numbers.append(num)  # add number to list
    numbers_tuple = tuple(numbers)  # convert list to tuple

print("\nThe 1st number is:", numbers_tuple[0])  # print the 1st number
print("The last number is:", numbers_tuple[-1])  # print the last number