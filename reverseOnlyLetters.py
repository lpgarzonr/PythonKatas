from queue import LifoQueue
 
def reverseOnlyLetters(string):
	stack = LifoQueue()
	reversedStr = ''

	for char in string:
		if char.isalpha():
			stack.put(char)

	for char in string:
		if char.isalpha():
			lastLetter = stack.get(char)
			reversedStr += lastLetter
		else:
			reversedStr += char
	return reversedStr

print('expect: Qedo1ct-eeLg=ntse-T!')

print(reverseOnlyLetters('Test1ng-Leet=code-Q!'))