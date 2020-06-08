def coinsCount(value):
	numberOfCoins = 0
	coinsValues = [25, 5, 1]

	for coinValue in coinsValues:
		coins = getNumberOfCoins(value, coinValue)
		numberOfCoins += coins
		value -= coins * coinValue
		if value == 0:
			break
	return numberOfCoins

def getNumberOfCoins(value, coinValue):
	return int(value/coinValue)

print(coinsCount(30))
print(coinsCount(4))
print(coinsCount(5))
print(coinsCount(1))
print(coinsCount(0))