def printPath(matrix):
	lastRowIdx = len(matrix) - 1
	lastColumnIdx = len(matrix[0]) - 1
	path = []
	getPath(matrix, lastRowIdx, lastColumnIdx, path)
	print(path)

def getPath(matrix, rowIndex, columnIndex, path):
	if rowIndex < 0 or columnIndex < 0:
		return False
	if matrix[rowIndex][columnIndex] == 0:
		return False

	if rowIndex == 0 and columnIndex == 0:
		path.append(' '+str(rowIndex) + ',' + str(columnIndex))
		return True
    
	rowPath = getPath(matrix, rowIndex-1, columnIndex, path)
	if rowPath == True:
		path.append(' '+str(rowIndex) + ',' + str(columnIndex))
	return True

	columnPath = getPath(matrix, rowIndex, columnIndex -1, path)
	if columnPath == True:
		path.append(' '+str(rowIndex) + ',' + str(columnIndex))
	return True

matrix = [
	[1,0,0],
	[1,1,1],
	[0,1,0],
	[0,1,1],
	[0,0,1],
]

printPath(matrix)