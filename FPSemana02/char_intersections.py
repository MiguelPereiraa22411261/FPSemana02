word2 = ""
while True:
    print("Input the first word.")
    word1 = input()
    if " " in word1:
        print("Word contains spaces in between! Please input the word again without spaces.")
    elif word1 == "":
        print("This is not a valid input!")
    else:
        while True:
            print("Input the second word.")
            word2 = input()
            if " " in word2:
                print("Word contains spaces in between! Please input the word again without spaces.")
            elif word2 == "":
                print("This is not a valid input!")
            else:
                break
        break
setword1 = set(word1)
setword2 = set(word2)

result = [] # Allows the use of result.sort() unlike result = ""

intersection = setword1.intersection(setword2) # Creates an intersection between words
for char in intersection:
    result += char
result.sort(key=lambda x: (x.islower(), x)) # Always puts uppercase letters first
for char in result:
    print(char, end = "") # Shows every character in the same line