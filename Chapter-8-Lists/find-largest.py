# Find the largest number in a list

count = int(input("Enter how many numbers you want to enter: "))  # input number of elements
numbers = []  # initialize an empty list to store numbers

for i in range(count):  # loop to input numbers
    try:
        num = float(input("Enter number " + str(i + 1) + " : "))  # input each number
        numbers.append(num) # add the number to the list
        largest = max(numbers)  # find the largest number in the list
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
print("The largest number is: " + str(largest))  # print the largest number