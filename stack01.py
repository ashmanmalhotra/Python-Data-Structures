import os
import time

stack = []

def clearscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
        
def push(item):
    stack.append(item)

def pop():
    #return stack.pop()
    if isEmpty():
        return "The Stack is Empty."
    else:
        return stack.pop()

def isEmpty():
    return len(stack) == 0

def top():
    return stack[-1]


while True:
    print("Choose options 1-5 from following Stack Operations: ")
    print("1. Push")
    print("2. Pop")
    print("3. Is Empty") 
    print("4. Top Element")
    print("5. Quit")

    option = int(input("Enter option 1-5: "))
    if option not in [1, 2, 3, 4, 5]:
        clearscreen()
        print("You chose wrong option. Please try again...")
        time.sleep(3)
        clearscreen()
        continue

    if option == 1:
        clearscreen()
        num = int(input("Input the Numeric Item you wish to push into stack: "))
        push(num)
        time.sleep(1)
        clearscreen()
    elif option == 2:
        #if isEmpty():
        #    print("The Stack is Empty.")
        #else:
        #    print("The popped item: ", pop())
        print("The popped item: ", pop())
    elif option == 3:
        if isEmpty():
            print("The Stack is empty.")
        else:
            print("The stack is not empty.")


    elif option == 4:
        print("The top item in the stack is: ", top())
    else:
        break