class LinkedQueue:
    def __init__(self):
        self.list = LinkedNode()

    def enqueue(self, data):
        self.list.add(self.list.size - 1, data)

    def dequeue(self):
        return self.list.remove(idx=0)
