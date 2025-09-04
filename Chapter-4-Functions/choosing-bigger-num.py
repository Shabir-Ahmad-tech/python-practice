# Choose the bigger

def bigger_number (a, b):
    if a > b:
        return a
    else:
        return b
    
a = int(input("Enter the first number: "))  # input first number
b = int(input("Enter the second number: ")) # input second number

print("The bigger number is: " + str(bigger_number(a, b)))  # print bigger number