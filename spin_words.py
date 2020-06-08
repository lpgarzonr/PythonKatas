def spin_words(sentence):
	words = sentence.split()
	newWords = []
	for word in words:
		if len(word) > 4:
			newWords.append(word[::-1])
		else:
			newWords.append(word)
	return " ".join(newWords)

res = spin_words("This is another test")
print(res)