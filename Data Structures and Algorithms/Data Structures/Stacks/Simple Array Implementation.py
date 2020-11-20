# Implementation of Stack using Simple Array
# Stack Class
class Stack(object):
    # Initialize the stack
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

# Check if stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0

# Push New item in the stack
    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Stack Overflow!")
        else:
            self.stk.append(item)
        print("Stack after Push", self.stk)

# Pop the top item from the stack
    def pop(self):
        if(len(self.stk)) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk.pop()

# View Stack
    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk[::-1]

# Check the size of the stack
    def size(self):
        return len(self.stk)


# Create an object for Accessing the Stack Class and Perform all the operations of the stack class
our_stack = Stack()
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("3")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
