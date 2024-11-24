# dummy head 虚拟的头节点
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.dummy_head = Node(None, None)
        self.size = 0

    def add(self, idx, data):
        pred = self.dummy_head
        for i in range(idx):
            pred = pred.next

        pred.next = Node(data, pred.next)
        self.size += 1

    def remove_by_idx(self, idx):

        if idx - 1 > self.size:
            raise "参数错误"
        pred = self.dummy_head
        for i in range(idx):
            pred = pred.next
        data = pred.next.data
        pred.next = pred.next.next
        self.size -= 1
        return data

    def count(self):
        return self.size

    def get_by_idx(self, idx):

        if idx > self.size or idx < 0: raise "idx 参数错误"
        # dummy_head 要过滤掉
        pred = self.dummy_head.next
        for i in range(idx):
            pred = pred.next
        return pred.data

    def get_first(self):
        return self.get_by_idx(0)

    def get_last(self):
        return self.get_by_idx(self.size - 1)

    def set(self, idx, data):

        if idx > self.size or idx < 0: raise "idx 参数错误"

        pred = self.dummy_head.next
        for i in range(idx):
            pred = pred.next
        pred.data = data

    def contains(self, data):

        current = self.dummy_head.next
        for i in range(self.size):
            if current.data == data:
                return True

        return False


node_list = LinkedList()
node_list.add(0, 0)
node_list.add(1, 1)
node_list.add(2, 2)
print(node_list)

print(node_list.get_by_idx(0))
print(node_list.get_by_idx(1))

node_list.set(0, 10)

print(node_list.contains(10))
print(node_list.contains(11))

print(node_list.remove_by_idx(0))
print(node_list.remove_by_idx(0))
print(node_list.remove_by_idx(0))
