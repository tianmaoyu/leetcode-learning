from operator import itemgetter
from typing import no_type_check_decorator


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedNode:
    size: int = 0
    head: Node = None

    def __init__(self):
        self.head = Node(None, None)
        self.size = 0

    def add_first(self, data):
        node = Node(data, self.head)
        self.head=node
        self.size += 1

    def add(self, idx, data):
        if self.size==0:
            self.add_first(data)
        else:
            pred= self.head
            for i in range(idx-1):
                pred= pred.next
            node = Node(data,pred)
            node.next=pred.next
            pred.next=node
            self.size+=1

    def remove(self, data):

        if self.head.data==data:
            self.head=self.head.next
            return self.head

        pred=self.head
        while pred:
            if pred.data==data:
                pred=pred.next
                return pred
            pred=pred.next




    def __len__(self):
        return self.size


linked_list= LinkedNode()
linked_list.add_first(2)
linked_list.add_first(0)
linked_list.add(1,1)
print(linked_list)