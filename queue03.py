# Implementation of Queue using Double-Ended Queue from Collections Module

import collections
queue = collections.deque()       # Empty Queue

# Enqueue - Adding Elements 
def enqueue(item):
    queue.append(item)

# Dequeue - Removing Element from Head
def dequeue():
    return queue.popleft()

def sizeOf(dequeue):
    return len(dequeue)

def front():
    return queue[0]

def tail():
    return queue[-1]




