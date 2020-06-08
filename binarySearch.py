def findBybinarySearch(arr, element):
	res = binarySearch(arr, element, 0, len(arr) -1)
	print(res)

def binarySearch(arr, element, firstIdx, lastIdx):
	if lastIdx < firstIdx:
		return False
	middleIdxSubArray = (lastIdx - firstIdx) // 2
	middleIdx = firstIdx + middleIdxSubArray
	middleElement = arr[middleIdx]

	if middleElement == element:
		return True
	if element < middleElement:
		return binarySearch(arr, element, firstIdx, middleIdx - 1)
	else:
		return binarySearch(arr, element, middleIdx + 1, lastIdx)
	return False

findBybinarySearch([1,2,3,4], 1)
findBybinarySearch([1,2,3,4], 2)
findBybinarySearch([1,2,3,4], 3)
findBybinarySearch([1,2,3,4], 4)
findBybinarySearch([1,2,3,4], 5)
findBybinarySearch([1,2,3,4], 0)

0,