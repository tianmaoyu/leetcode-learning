
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedNode:
    size:int = 0
    head:Node = None

    def __init__(self):
        self.head =None
        self.size=0


    def add_frist(self,data) :
        node = Node(data)
        node.next=self.head
        self.size+=1
        self.head=node

    def remove(self,data) :
        self.head=self.head.next


    def __len__(self):
        return self.size
