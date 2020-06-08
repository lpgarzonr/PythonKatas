def getFirstDuplicatedChar(word):
    charsCounter = []
    for char in word:
        if char in charsCounter:
            return char;
        else:
            charsCounter.append(char)
    return 'No repited Char'

duplicatedChar = getFirstDuplicatedChar("din")
print(duplicatedChar)

duplicatedChar = getFirstDuplicatedChar("recede")
print(duplicatedChar)

duplicatedChar = getFirstDuplicatedChar("Success")
print(duplicatedChar)

duplicatedChar = getFirstDuplicatedChar("(( @")
print(duplicatedChar)