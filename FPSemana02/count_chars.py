while True:
    print("Input a phrase:")
    stringlol = input()
    
    if stringlol == " " or stringlol == "":
        print ("This is not a valid input.")
    
    else:
        
        # Read every single character inside the string 
        stringwords = [] 
        word = ""
        for char in stringlol: 
            if char.isalnum(): # If the character is alpha-numeric
                word += char # Add the character to the word being built
            else:
                if word: # If a word is built, add it to the stringwords list
                    stringwords.append(word)
                    word = "" # Resets the word
                if not char.isspace(): # If the character isn't a " " (meaning it is punctuation)
                    stringwords.append(char) # Add the punctuation seperately
        
        # If the last word isn't added
        if word:
            stringwords.append(word)
        
        # Literally just the dictionary    
        dictionary = {word: len(word) for word in stringwords}
        
        # Shows the dictionary
        print(dictionary)
        input()
        break