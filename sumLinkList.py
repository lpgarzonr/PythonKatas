class Node:
	next = None

	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return str(self.value)

seis = Node(6)
uno = Node(1)
nOneHead = Node(7)

nOneHead.next = uno
uno.next = seis

dos = Node(2)
nueve = Node(9)
nTwoHead = Node(5)

nTwoHead.next = nueve
nueve.next = dos

def sum(l1, l2, carry = 0):
	if l1 == None and l2 == None:
		return None

	value = carry
	if l1 != None:
		value += l1.value
	if l2 != None:
		value += l2.value

	carry = 1 if value > 9 else 0
	result = Node(value%10)
	result.next = sum(l1.next, l2.next, carry)
	print(result)

sum(nOneHead, nTwoHead)



