# Implementation of Queue using Class Method

class Queue:
    def __init__(self):
        self.queue = []
    
    # Enqueue Operation
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue Operation
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def displayQueue(self):
        return self.queue

    def size(self):
        return len(self.queue)

qq = Queue()
qq.enqueue(10)
qq.enqueue(20)
qq.enqueue(30)

print("The elements of the Queue: ", qq.displayQueue())

print("Dequeued Element: ", qq.dequeue())
print("Queue Elements After Dequeue Operation: ", qq.displayQueue())