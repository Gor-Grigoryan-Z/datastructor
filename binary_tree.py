from collections import deque


class Node:
	def __init__(self, value) -> None:
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)

class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self, node):
		if not isinstance(node, Node):
			node = Node(node)

		if self.root is None:
			self.root = node
		else:
			self._insert(self.root, node)

	def _insert(self, current, node):
		if current.value > node.value:
			if current.left is None:
				current.left = node
			else:
				self._insert(current.left, node)
		else:
			if current.right is None:
				current.right = node
			else:
				self._insert(current.right, node)

	def preOrder(self):
		self._preOrder(self.root)

	def _preOrder(self, current):
		if current:
			print(current.value)
			self._preOrder(current.left)
			self._preOrder(current.right)

	def postOrder(self):
		self._postOrder(self.root)

	def _postOrder(self, current):
		if current:
			self._postOrder(current.left)
			print(current.value)
			self._postOrder(current.right)

	def levelOrder(self):
		if not self.root:
			return

		queue = deque()
		queue.append(self.root)

		while queue:
			node = queue.popleft()
			print(node, end=" ")

			if node.left:
				queue.append(node.left)

			if node.right:
				queue.append(node.right)

	def inOrder(self):
		self._inOrder(self.root)

	def _inOrder(self, current):
		if current:
			self._postOrder(current.left)
			self._postOrder(current.right)
			print(current.value)

	def search(self, value):
		return self._search(self.root, value)

	def _search(self, currentElement, value):
		if currentElement:
			if currentElement.value == value:
				return currentElement.value
			elif currentElement.value > value:
				return self._search(currentElement.left, value)
			else: 
				return self._search(currentElement.right, value)
		return "Element not found"
	
	def delete(self, value):
		self._delete(self.root, value, None, None)
		
	def _delete(self, current, value, previous, isLeft):
		if current:
			if current.value == value:
				if current.left is None and current.right is None:
					if previous:
						if isLeft:
							previous.left = None
						else:
							previous.right = None
					else:
						self.root = None
				elif current.left is None:
					if previous:
						if isLeft:
							previous.left = current.right
						else:
							previous.right = current.right
					else:
						self.root = current.right
				elif current.right is None:
					if previous:
						if isLeft:
							previous.left = current.left
						else:
							previous.right = current.left
					else:
						self.root = current.left
				else:
					minRight = self.getMinFromRightSideInTree(current.right)
					current.value = minRight.value
					self._delete(current.right, minRight.value, current, False)
			elif value < current.value:
				return self._delete(current.left, value, current, True)
			elif value > current.value:
				return self._delete(current.right, value, current, False)


    
	def getMinFromRightSideInTree(self, current):
		if current.left is None:
			return current
		else:
			return self.getMinFromRightSideInTree(current.left)


tree = BinaryTree()
tree.insert(100)
tree.insert(50)
tree.insert(400)
tree.insert(300)

print(tree.postOrder())
print(tree.delete(50))
print(tree.search(50))
print("----------------------------------------------------")
print("----------------------------------------------------")
print(tree.inOrder())
tree.levelOrder()