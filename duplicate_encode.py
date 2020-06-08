def duplicate_encode(wordAnyCase):
    word = wordAnyCase.lower()
    charsCounter = {}
    for chari in word:
        char = chari
        if char in charsCounter:
            charsCounter[char] = 2
        else:
            charsCounter[char] = 1
    return encode_word(word, charsCounter)

def encode_word(word, charsCounter):
    oneTimeChar = '('
    duplicatedChar = ')'
    encodedWord = ''
    for char in word:
        if charsCounter[char] == 1:
            encodedWord = encodedWord + oneTimeChar
        else:
            encodedWord = encodedWord + duplicatedChar
    print(charsCounter)
    return encodedWord

encoded = duplicate_encode("din")
print(encoded)

encoded = duplicate_encode("recede")
print(encoded)

encoded = duplicate_encode("Success")
print(encoded)

encoded = duplicate_encode("(( @")
print(encoded)