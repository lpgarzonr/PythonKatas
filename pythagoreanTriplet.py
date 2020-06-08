def hasPythagoreanTriplet(arr):
	n = len(arr)
	if n < 3:
		return False
	for i in range(0, n-2):
		element1 = arr[i] * arr[i]
		for j in range(i+1, n-1):
			element2 = arr[j] * arr[j]
			for k in range(i+2, n):
				res = arr[k] * arr[k]
				isPythagoreanTreiple = element1 + element2 == res
				if isPythagoreanTreiple:
					return True
	return False

print(hasPythagoreanTriplet([4, 3, 5]))
print(hasPythagoreanTriplet([1, 4, 0, 3, 5]))
print(hasPythagoreanTriplet([1, 2, 0, 3, 20]))
print(hasPythagoreanTriplet([]))

