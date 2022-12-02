# Implementation of Queue using the deque class of Collections Library
import collections

queue = collections.deque()

# Add Elements from Left
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)

# Dequeue Operation - Head is towards the extreme Right Side
queue.pop()   # 10
queue.pop()   # 20
queue.pop()   # 30

# Addition of Elements from Right Direction - Tail is toward Extreme Right side
# HEad is towards extreme left side
# Addition of Elements
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue Operation - Head at extreme Left
queue.popleft()   # 10
queue.popleft()   # 20
queue.popleft()   # 30

# Retrieve Head When Head is at Extreme Left
print(queue[0])

# Retrieve Tail When Tail is at Extreme Right
print(queue[-1])


