print("Input the first word")
word1 = input()
print("Input the second word")
word2 = input()

setword1 = set(word1)
setword2 = set(word2)

result = []

intersection = setword1.intersection(setword2)
for char in intersection:
    result += char
result.sort(key=lambda x: (x.islower(), x))
for char in result:
    print(char, end = "")