# Count the number of lines in a file

file = open("story.txt", "r")   # open file in read mode
count = 0                       # initialize count to 0
for line in file:               # read file line by line   
    count += 1                  # increment count for each line    
print("Number of lines in the file: " + str(count))  # print number of lines
file.close()                    # close the file
