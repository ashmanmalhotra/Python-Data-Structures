# Implementing Stack with deque() class from collections library
import collections

def create_stack():
    stack = collections.deque()
    return stack

def empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Pushed Item: ", item)

def pop(stack):
    if (empty(stack)):
        return "The Stack is Empty..."
    
    return stack.pop()

def top(stack):
    if (empty(stack)):
        return "The Stack is Empty..."
    
    return stack[-1]    


stack = create_stack()
# Pushing Elements into the stack
push(stack, 10)
push(stack, 20)
push(stack, 30)

# Pop Elements from the Stack
print(pop(stack))

# Top Element of the Stack
print(top(stack))

# Pop the remaining Elements from the Stack
print(pop(stack))
print(pop(stack))