def multiplyNumbers(numA, numB):
	small = numA if numA < numB else numB
	big = numA if numA > numB else numB
	return multiply(big, small)

def multiply(baseNum, timesNum):
	if baseNum == 0:
		return 0
	if timesNum == 1:
		return baseNum

	halffTimes = timesNum // 2
	halfSum = multiply(baseNum, halffTimes)
	res = (timesNum % 2)
	if res == 0:
		return halfSum + halfSum
	return halfSum + halfSum + baseNum

print(multiplyNumbers(4, 3))