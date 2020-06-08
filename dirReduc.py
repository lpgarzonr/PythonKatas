def dirReduc(directions):
	finalDirections = [None]
	n = "NORTH"
	s = "SOUTH"
	w = "WEST"
	e = "EAST"
	for direction in directions:
		if direction == n and finalDirections[-1] == s or direction == s and finalDirections[-1] == n or direction == w and finalDirections[-1] == e or direction == e and finalDirections[-1] == w:
			finalDirections.pop()
		else:
			finalDirections.append(direction)
	return finalDirections[1:]

a = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))
