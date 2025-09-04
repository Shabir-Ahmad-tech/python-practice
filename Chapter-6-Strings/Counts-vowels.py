

name = input("Enter a name: ")  # input string

def count_vowels(name):
    count = 0
    vowels = "aeiouAEIOU"
    for char in name:
        if char in vowels:
            count += 1
    return count

vowel = count_vowels(name)
print("Number of vowels in the name: " + str(vowel))  # print number of vowels