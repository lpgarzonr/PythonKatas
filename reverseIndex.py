class LinkedLis:
	head = None
	valueInNIndex = None
	
	def __init__(self, head):
		self.head = head

	def lastN(self, n, node):
		if node == None:
			return 0;
		reverseIndex = self.lastN(n, node.next) + 1
		if reverseIndex == n:
			self.valueInNIndex = node.value
		return reverseIndex

	def findLastN(self, n):
		self.valueInNIndex = None
		self.lastN(n, self.head)

	def printLastN(self):
		if self.valueInNIndex == None:
			print("not found")
		else:
			print("value %s"%(self.valueInNIndex))

class Node:
	next = None
	reverNValue = None

	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return str(self.value)

seis = Node(6)
uno = Node(1)
siete = Node(7)
tres = Node(3)

seis.next = uno
uno.next = siete
siete.next = tres

list = LinkedLis(seis)
list.findLastN(5)
list.printLastN()

list.findLastN(1)
list.printLastN()


list.findLastN(3)
list.printLastN()