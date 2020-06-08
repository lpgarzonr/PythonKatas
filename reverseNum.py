def reverse(x):
	powValue = len(str(abs(x))) - 1
	isNegative = x < 0
	reversedNumber = getReverseValue(abs(x), powValue)
	return -reversedNumber if isNegative else reversedNumber

def getReverseValue(x, powValue):
	if x < 10:
		return x
	lastDigit = x % 10
	newNumber = x // 10
	return lastDigit * pow(10, powValue) + getReverseValue(newNumber, powValue-1)

print(reverse(123))
print(reverse(-123))
print(reverse(120))