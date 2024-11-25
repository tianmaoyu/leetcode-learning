class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# 二叉搜索树
class BinaryTreeSearch:
    def __init__(self):
        self.size=0
        self.root:Node=None

    def add(self,data):
       self.root= self._add(self.root,data)

    def _add(self,root,data):
        if root is None:
            root=Node(data)
            self.size+=1
            return root

        if root.data > data:
           root.left= self._add(root.left,data)
        elif root.data < data:
           root.right= self._add(root.right,data)

        return root

    def min(self):
        return self._min(self.root)

    def _min(self,root):
        if root.left is None:
            return root.data
        return self._min(root.left)

    def max(self):
        return self._max(self.root)
    def _max(self,root):
        if root.right is None:
            return root.data
        return self._max(root.right)

    def remove(self,data):
        pass

    def remove_min(self):
        min = self.min()
        self.root = self._remove_min(self.root)
        return min

    # 困难点
    def _remove_min(self,node):
        if node.left is None:
            right_node= node.right
            node.right=None
            self.size-=1
            return right_node

        node.left=self._remove_min(node.left)
        return node



    def pre_order(self):
        """
        前序遍历
        :return:
        """
        array=[]
        self._pre_order(self.root,array)
        return array

    def _pre_order(self,root,array:list=[]):

        if root is None:
            return

        array.append(root.data)
        self._pre_order(root.left,array)
        self._pre_order(root.right,array)



    def mid_order(self):
        """
        中序遍历
        :return:
        """
        array=[]
        self._mid_order(self.root,array)
        return array

    def _mid_order(self,root,array):
        if root is None:
            return
        self._mid_order(root.left, array)
        array.append(root.data)
        self._mid_order(root.right, array)

    def post_order(self):
        """
        后序遍历
        :return:
        """
        array=[]
        self._post_order(self.root,array)
        return array

    def _post_order(self,root,array):
        if root is None:
            return

        self._post_order(root.left,array)
        self._post_order(root.right,array)
        array.append(root.data)



tree=BinaryTreeSearch()
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(1.5)
tree.add(0)
print(tree)

print(tree.min())
print(tree.max())
print(tree.pre_order())
print(tree.mid_order())
print(tree.post_order())
print(tree.remove_min())
print(tree)