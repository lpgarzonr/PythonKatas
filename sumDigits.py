def sumDigits(strNumber):
	if strNumber == None or len(strNumber) == 0:
		return 0
	if len(strNumber) == 1:
		return int(strNumber)
	else:
		return int(strNumber[0]) + sumDigits(strNumber[1:])
print("expected 10: ")
print(sumDigits("1234"))
print("expected 4: ")
print(sumDigits("22"))
print("expected 0: ")
print(sumDigits(None))
print("expected 43: ")
print(sumDigits("9925738"))


def sumDigitsInNumber(number):
	if number <= 10:
		return number

	numberToSum = number % 10
	newNumber = (number - numberToSum) / 10
	return numberToSum + sumDigitsInNumber(newNumber)

print("expected 10: ")
print(sumDigitsInNumber(1234))
print("expected 4: ")
print(sumDigitsInNumber(22))
print("expected 0: ")
print(sumDigitsInNumber(0))
print("expected 43: ")
print(sumDigitsInNumber(9925738))