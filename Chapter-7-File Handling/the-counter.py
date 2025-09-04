# Open a file and count the number of "the" in it

name = input("Enter file name: ")  # input file name
try: 
    file = open(name, "r")   # open file in read mode
except:
    print("File not found. Please check the file name and try again.")
    exit()
count = 0                       # initialize count to 0
for line in file:               # read file line by line   
    if "the" in line.lower():   # check if "the" is in the line
        count += 1              # increment count if "the" is found
print("Number of times 'the' appears in the file: " + str(count))  # print number of "the"
file.close()                        # close the file