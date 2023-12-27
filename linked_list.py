class Node:
	def __init__(self, value) -> None:
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def addToStart(self, value):
		if not isinstance(value, Node):
			value = Node(value)

		if self.head is None:
			self.head = value
			self.tail = value
		else:
			value.next = self.head
			self.head = value
		
	def addToEnd(self, value):
		if not isinstance(value, Node):
			value = Node(value)

		if self.tail is None:
			self.tail.next = value
			self.tail = value

	def pop(self):
		if self.head is None:
			return None
		
		currentElement = self.head
		self.head = self.head.next
		return currentElement
	
	def search(self, value):
		if self.head is None:
			return None
		
		currentElement = self.head
		while currentElement:
			if currentElement.value == value:
				return currentElement

			currentElement = currentElement.next

		return "Element not found"
	
	def delete(self, value):
		if self.head is None:
			return
		
		if self.head.value == value:
			self.head = self.head.next
		else:
			currentElement = self.head
			while currentElement:
				if currentElement.next is not None:
					if currentElement.next.value == value:
						currentElement.next = currentElement.next.next
				currentElement = currentElement.next

	def __str__(self) -> str:
		currentElement = self.head
		output = ""
		while currentElement:
			output += (str(currentElement.value) + "--->")
			currentElement = currentElement.next
		return output
	

linkedList = LinkedList()

linkedList.addToStart(10)
linkedList.addToStart(20)
linkedList.addToStart(30)

print(linkedList)
linkedList.delete(10)
print(linkedList)
