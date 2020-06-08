def dispatcher(sensorValues1, sensorValues2, size):
	if size == 0:
		return 0
	absValue = abs(sensorValues2[size-1]) - abs(sensorValues1[size-1])
	return absValue + dispatcher(sensorValues1, sensorValues2, size-1)

print(dispatcher([],[], 0))

print(dispatcher([1,2,3],[-2,3,-4], 3))