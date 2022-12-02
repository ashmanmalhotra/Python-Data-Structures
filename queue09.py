# Implementing the Priority Queue - Based on the Larger and Smaller Values

class PriorityQueue:
    def __init__(self, priority="low"):
        """
        priority: high | low
                    high: The items with higher value will be piroritised.
                    low: The items with lower value will be piroritised.
        """
        self.__priority = priority
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def head(self):
        if not self.isEmpty():
            if self.__priority == 'low':
                return self.queue[0]
            return self.queue[-1]
        return None

    def tail(self):
        if not self.isEmpty():
            if self.__priority == 'low':
                return self.queue[-1]
            return self.queue[0]
        return None

    def dequeue(self):
        if not self.isEmpty():
            if self.__priority == 'low':
                return self.queue.pop(0)
            return self.queue.pop()
        return None

    def enqueue(self, item):
        if self.isEmpty():
            self.queue.append(item)
        else:
            self.queue.append(item)
            self.queue.sort()


obj = PriorityQueue(priority="high")

# Test: Whether the Queue is Empty?
print("Queue is Empty") if obj.isEmpty() == True else print("Queue is Not Empty")

# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)

# Test: Head() Operation from Empty Queue
result = obj.head()
print("Head - Queue is Empty") if result == None else print("Head Element: ", result)

# Test: Tail() Operation from Empty Queue
result = obj.tail()
print("Tail - Queue is Empty") if result == None else print("Tail Element: ", result)

# Test - Enqueue Operation
print("Enqueue Elements - 101, 10, 1 and 9.")
obj.enqueue(101)
obj.enqueue(10)
obj.enqueue(1)
obj.enqueue(9)

# Print the element after Enqueue Operation
print("Elements after Enqueue Operation: ", obj.queue)

# Test: Whether the Queue is Empty?
print("Queue is Empty") if obj.isEmpty() == True else print("Queue is Not Empty")

# Test: Head() Operation from Empty Queue
result = obj.head()
print("Head - Queue is Empty") if result == None else print("Head Element: ", result)

# Test: Tail() Operation from Empty Queue
result = obj.tail()
print("Tail - Queue is Empty") if result == None else print("Tail Element: ", result)

# Performing Dequeue Operation after Enqueue of 4 random elements
# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)

# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)

# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)

# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)

# Test: Dequeue() Operation from Empty Queue
result = obj.dequeue()
print("Queue is Empty") if result == None else print("Dequeued Element: ", result)