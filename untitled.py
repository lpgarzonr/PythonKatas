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

duplicatedChar = duplicate_encode("recede")
print(duplicatedChar)

duplicatedChar = duplicate_encode("Success")
print(encodduplicatedChared)

duplicatedChar = duplicate_encode("(( @")
print(duplicatedChar)