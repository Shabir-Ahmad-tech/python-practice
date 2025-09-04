# Ask the user for name and print the first and last character of the name

name = input("Enter your name: ")  # input name

def first_and_last_char(name):
    if len(name) == 0:
        return "Invalid input"
    elif len(name) > 1:
        return name[0], name[-1]

first, last = first_and_last_char(name)

print("First character: " + first)  # print first character
print("Last character: " + last)    # print last character