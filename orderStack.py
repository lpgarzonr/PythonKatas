from queue import LifoQueue

def sortStack(stack):
	tempStack = LifoQueue()

	while stack.empty() == False:
		elementToOrder = stack.get()
		compareWithTempStack(elementToOrder, stack, tempStack)
	while tempStack.empty() == False:
		stack.put(tempStack.get())

def compareWithTempStack(elementToOrder, stack, tempStack):
	if tempStack.empty():
		tempStack.put(elementToOrder)
	else:
		tempStackElement = tempStack.get()
		if elementToOrder >= tempStackElement:
			tempStack.put(tempStackElement)
			tempStack.put(elementToOrder)
		else:
			stack.put(tempStackElement)
			compareWithTempStack(elementToOrder, stack, tempStack)

def printStack(stack):
	while stack.empty() == False:
		print(stack.get())

stack = LifoQueue()
stack.put(5)
stack.put(3)
stack.put(4)
stack.put(1)
stack.put(2)

sortStack(stack)
printStack(stack)
