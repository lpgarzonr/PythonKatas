def in_array(array1, array2):
	result = set()
	for str1 in array1:
		if any(str1 in str2 for str2 in array2):
			result.add(str1)
	return sorted(list(result))

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))