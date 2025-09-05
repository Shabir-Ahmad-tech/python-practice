# Asks for name, age and country and prints age using dictionary

# Asks for name, age and country and prints age using dictionary

info = {}  # create an empty dictionary
nums = int(input("Enter number of people: "))  # input number of people
for i in range(nums): # loop to input name, age and country
    name = input("Enter name " + str(i + 1) + ": ")  # input name
    age = input("Enter age " + str(i + 1) + ": ")  # input age
    country = input("Enter country " + str(i + 1) + ": ")  # input country
    info[name] = {"age": age, "country": country}  # add name, age and country to dictionary

print("\nInformation are stored")
print("The information of the people are:")

for name, details in info.items():
    print(f"Name: {name}, Age: {details['age']}, Country: {details['country']}")  # print name, age and country