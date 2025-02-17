class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return("Empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return("Empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Examples on how to use

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Queue after enqueuing: {queue}")
print(f"Front item: {queue.peek()}")
print(f"Dequeued item: {queue.dequeue()}")
print(f"Queue after dequeuing: {queue}")
print(f"Is queue empty? {queue.is_empty()}")
