# dummy head 虚拟的头节点
class Node:
    def __init__(self,data,next_node):
        self.data=data
        self.next=next_node

class LinkedList:
    def __init__(self):
        self.dummy_head=Node(None,None)
        self.size=0

    def add(self,idx,data):
        pred = self.dummy_head
        for i in range(idx):
            pred=pred.next

        pred.next= Node(data,pred.next)
        self.size+=1

    def remove_by_idx(self,idx):

        if idx-1 > self.size:
            return None

        pred = self.dummy_head
        for i in range(idx):
            pred = pred.next

        data=pred.next.data
        pred.next=pred.next.next
        return data

    def count(self):
        return self.size


node_list=LinkedList()
node_list.add(0,0)
node_list.add(1,1)
node_list.add(2,2)
print(node_list)

print(node_list.remove_by_idx(0))
print(node_list.remove_by_idx(0))
print(node_list.remove_by_idx(0))
