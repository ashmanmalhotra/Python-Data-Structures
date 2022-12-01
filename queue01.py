# Implementing Queue Using List
import os
import time

queue = []

def clearscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

def enqueue(item):
    queue.append(item)
    

def dequeue():
    return queue.pop(0)

def isEmpty():
    return len(queue) == 0

#def isFull():
#    pass

def front():
    return queue[0]

def tail():
    return queue[-1]


while True:
    clearscreen()
    print("Select option 1-5 from following operations: ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Is Empty")
    print("4. Front Element")
    print("5. Rear Element")
    print("6. Quit")
    option = int(input("Enter the option 1-6: "))
    if option not in list(range(1, 7)):
        clearscreen()
        print("Wrong option selected. Please try again...")
        time.sleep(3)
        continue

    clearscreen()
    if option == 1:
        item = int(input("Enter the element you want to insert into the queue: "))
        enqueue(item)
        print("The insertion operation is completed.")
    elif option == 2:
        if isEmpty():
            print("The Queue is empty...")
        else:
            print("The element removed from the queue: ", dequeue())
    elif option == 3:
        if isEmpty():
            print("The Queue is empty...")
        else:
            print("The Queue is not Empty...")
    elif option == 4:
        if isEmpty():
            print("The Queue is empty...")
        else:
            print("Queue - Front Element: ", front())
    elif option == 5:
        if isEmpty():
            print("The Queue is empty...")
        else:
            print("Queue - Rear Element: ", tail())        
    else:
        break

    time.sleep(3)
