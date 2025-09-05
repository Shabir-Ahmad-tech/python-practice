# Split sentence into words

sentence = input("Enter a sentence: ")  # input sentence
words = []
s_split = sentence.split() # split sentence into words
for word in s_split:  # loop through each word in the split sentence
    words.append(word)  # add each word to the list

# print("The words in the sentence are: " + str(words))  # print the list of words

print("The words in the sentence are: ")  # print the list of words
for word in words:
    print(word)  # print each word on a new line