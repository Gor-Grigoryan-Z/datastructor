class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            value.next = self.head
            self.head = value

    def pop(self):
        currentElement = self.head
        self.head = self.head.next
        return currentElement

    def peek(self):
        return self.head

    def search(self, value):
        if self.head is None:
            return "Value not found"

        currentElement = self.head
        while currentElement:
            if currentElement.value == value:
                return currentElement.value
            currentElement = currentElement.next

        return "Value not found"

    def __str__(self):
        if self.head is None:
            return "Stack is empty"

        output = ""
        currentElement = self.head
        while currentElement:
            output += str(currentElement.value)
            output +="\n|\n"
            currentElement = currentElement.next
        return output

myStack = Stack()

myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.push(50)
print(myStack)