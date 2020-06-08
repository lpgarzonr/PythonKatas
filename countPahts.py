def countPaths(row, column):
	if row == 1 or column == 1:
		return 1
	return countPaths(row - 1, column) + countPaths(row, column - 1)

print(countPaths(3, 3))
print(countPaths(2, 3))
