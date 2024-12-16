class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return("empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return("empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example on how to use it

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack after pushing: {stack}") 
print(f"Let's take a peek on the top: {stack.peek()}")      
print(f"Popped item: {stack.pop()}")   
print(f"Stack after popping: {stack}") 
print(f"Is stack empty? {stack.is_empty()}")  
