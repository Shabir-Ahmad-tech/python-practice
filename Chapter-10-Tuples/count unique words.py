# Use tuple to count unique words in a sentence

sentence = input("Enter a sentence: ")  # input sentence from user

words = sentence.split()  # split sentence into words
unique_words = tuple(set(words))  # convert list of words to a set to get unique words, then to a tuple

print("\nUnique words in the sentence is:")  # print message
for word in unique_words:
    # print those words which appear more than once in the sentence
    if words.count(word) > 1:
        print("The unique words are :",word)
        print("The word:",word,"appears:",words.count(word),"times")