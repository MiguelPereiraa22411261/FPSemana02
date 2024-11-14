print("Input the first word")
word1 = input()
print("Input the second word")
word2 = input()

setword1 = set(word1)
setword2 = set(word2)

intersection = setword1.intersection(setword2)
print(intersection)