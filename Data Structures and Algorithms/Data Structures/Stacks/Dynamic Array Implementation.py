# Implementation of Stack using Dynamic Array
# Stack Class
class Stack(object):
    # Initialize the stack
    def __init__(self, limit=10):
        self.stk = []    # Initializing the stack
        self.limit = limit

    # Check if the stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0

    # Push new item into the stack
    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print("Stack after push", self.stk)

    # Pop the item from the stack
    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk.pop()

    # See the stack
    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk[::-1]

    # Check the size of the array
    def size(self):
        return len(self.stk)

    # Resizing the stack - Using Repeated Doubling
    def resize(self):
        newStk = list(self.stk)
        self.limit = 2*self.limit
        self.stk = newStk


# Create object to perform operations
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")
our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.size())

# Too many doublings may cause memory overflow exception
