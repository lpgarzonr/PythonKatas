def is_isogram(string):
	duplicatedChars = []
	isIsogram = True
	lowercaseString = string.lower()
	for char in lowercaseString:
		if char in duplicatedChars:
			isIsogram = False
			break
		duplicatedChars.append(char)
	return isIsogram

string = "moOse"
res = is_isogram(string)
print(string, res)
