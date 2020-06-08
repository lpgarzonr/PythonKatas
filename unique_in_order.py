def unique_in_order(iterable):
	result = []
	shouldAddElement = lambda e: (len(result) == 0 or result[-1] != e)
  	for element in iterable:
		if shouldAddElement(element):
  			result.append(element)
  	return result;
  	
print(unique_in_order('AAAABBBCCDAABBB'))