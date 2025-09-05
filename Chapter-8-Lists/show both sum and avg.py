# Ask for numbers, then show both sum and average

number = int(input("How many numbers do you want to enter? "))  # input number of elements
numbers = []  # initialize an empty list to store numbers
total = 0  # initialize total to 0

for i in range(number):  # loop to input numbers
    try:
        num = float(input("Enter number " + str(i + 1) + ": "))  # input each number
        numbers.append(num)  # add the number to the list
        total = total + num  # add the number to total
        average = total / len(numbers)  # calculate average
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

print("The sum of the numbers are: " + str(total))  # print the sum of numbers
print("The average of the numbers are: " + str(average))  # print the average of numbers