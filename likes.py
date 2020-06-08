def likes(names):
	if names == None or type(names) != list:
		return None
	namesCount = len(names)
	if namesCount ==  0:
		return "no one likes this"
	if namesCount ==  1:
		return "%s likes this"%(names[0])
	if namesCount ==  2:
		return "%s like this"%(" and ".join(names))
	if namesCount ==  3:
		return "%s, %s like this"%(names[0], " and ".join(names[1:]))

	otherPersonsCount = namesCount - 2
	return "%s and %s others like this"%(", ".join(names[:2]), str(otherPersonsCount) )

print(likes(["Alex", "Jacob", "Mark", "Max"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Max", "John"]))
print(likes(["Mami"]))
print(likes([]))