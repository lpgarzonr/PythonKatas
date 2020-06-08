def findPath(maze, rowIdx, columnIdx, path):
	lastRowIdx = len(maze[0]) -1
	lastColumnIdx = len(maze) -1

	if rowIdx == lastRowIdx and lastColumnIdx == columnIdx:
		print(path)
		return True

	if rowIdx >= lastRowIdx or columnIdx >= lastColumnIdx or maze[rowIdx][columnIdx] == 0:
		return False

	path += '- '+ str(rowIdx) + ','+ str(columnIdx)
	rightPath = findPath(maze, rowIdx, columnIdx + 1, path);
	bottomPath = findPath(maze, rowIdx + 1, columnIdx, path);
	if rightPath == True or bottomPath == True:
		return True
	return False

matrix = [
	[1,0,0],
	[1,1,0],
	[0,1,1],
	[0,0,1],
	[0,0,1],
]

print(findPath(matrix, 0, 0, ''))