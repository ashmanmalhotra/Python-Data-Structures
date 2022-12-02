class QueueLR:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue)==0

    def head(self):
        if not self.isEmpty():
            return self.queue[-1]    # Head Element at extreme Right Direction
        return None

    def tail(self):
        if not self.isEmpty():
            return self.queue[0]    # Head Element at extreme Right Direction
        return None

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop()
        return None


objqueue = QueueLR()
# Testing Whether the Queue is Empty
if objqueue.isEmpty():
    print("The Queue is Empty")
else:
    print("The Queue is not Empty.")

objqueue.enqueue(10)
objqueue.enqueue(11)
objqueue.enqueue(12)

print(objqueue.queue)

objqueue.dequeue()
objqueue.dequeue()
objqueue.dequeue()
objqueue.dequeue()

print(objqueue.queue)

objqueue.enqueue(12)
result = objqueue.dequeue()
if result is None:
    print("Nothing to Dequeue.")
else:
    print("Dequeued Item: ", result)