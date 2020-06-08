class Node:
	def __init__(self, value):
		self.info = value
		self.link = None

class SingleLinkedList:
	def __init__(self):
		self.start = None

	def displayList(self):
		if self.start is None:
			print("List empty")
		else:
			print("List is: ")
			p = self.start
			while p is not None:
				print(p.info)
				p = p.link

	def createList(self):
		nodeOne = Node(1)
		nodeTwo = Node(2)
		nodeThree = Node(3)
		nodeFour = Node(4)
		nodeOne.link = nodeTwo
		nodeTwo.link = nodeThree
		nodeThree.link = nodeFour
		self.start = nodeOne

	def countElements(self):
		p = self.start
		n = 0
		while p is not None:
			n += 1
			p = p.link
		print("Elements:", n)

	def search(self, value):
		p = self.start
		n = 0
		while p is not None:
			if p.info == value:
				print("Found at pos:", n)
				break;
			n += 1
			p = p.link



list = SingleLinkedList()
list.createList()
list.displayList()
list.search(4)


