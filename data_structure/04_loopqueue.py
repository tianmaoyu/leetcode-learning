class LoopQueue:
    data: list = []
    front: int = 0
    tail: int = 0
    capacity: int = 0
    size: int = 0

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.front == self.tail

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.front

    def enqueue(self, value):
        if self.is_full():
            self.resize(len(self.data) * 2)

        self.size += 1
        self.tail = (self.tail + 1) % self.size
        if len(self.data) <= self.tail: self.data.append(value)
        else: self.data[self.tail]=value


    def dequeue(self):
        if self.is_empty(): return None

        front = self.data[self.front]
        self.front = (self.front + 1) % self.size
        self.size -= 1
        return front

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i, item in enumerate(self.data):
            new_data[i] = item
        self.data = new_data
        self.capacity = new_capacity


loopQueue = LoopQueue(3)
loopQueue.enqueue(1)
loopQueue.enqueue(2)
loopQueue.enqueue(3)
print(loopQueue.data)

loopQueue.enqueue(4)
print(loopQueue.data)

print(loopQueue.dequeue())
print(loopQueue.data)
print(loopQueue.dequeue())
print(loopQueue.data)
print(loopQueue)