print("Input a phrase:")
stringlol = input()

stringsplit = stringlol.split()

dictionary = {word: len(stringsplit) for word in stringsplit}
print(dictionary)