# Implementing the Priority Queue - The Lowest Item with the Highest Priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if self.isEmpty():
            self.queue.append(item)
        else:
            self.queue.append(item)
            self.queue.sort()

    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None
    
# Further Extension should be done by the students

q = PriorityQueue()

# Test Whether the Queue is Empty
if q.isEmpty():
    print("The Queue is Empty.")
else:
    print("The queue is not Empty")

# Performing the enqueue Operation
q.enqueue(50)
q.enqueue(60)
print("Queue after inserting 50 and 60: ", q.queue)
q.enqueue(1)
q.enqueue(11)
q.enqueue(5)
print("Queue after inserting 1, 11 and 5: ", q.queue)

# Test Whether the Queue is Empty
if q.isEmpty():
    print("The Queue is Empty.")
else:
    print("The queue is not Empty")

# Dequeue Operation on Queue
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())