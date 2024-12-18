from .time_logger import time_logger


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self._get_height = 1


class AVLTree:
    
    def __init__(self):
        self.root = None
    
    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.root == other.root
        else:
            return NotImplemented
    
    def __ne__(self, other) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
    
    def __gt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.root > other.root
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.root >= other.root
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.root < other.root
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.root <= other.root
        else:
            return NotImplemented

    def _get_height(self, node):
        if not node:
            return 0
        return node._get_height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    @time_logger
    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root._get_height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # Left rotation
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    @time_logger
    def delete(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_data_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if not root:
            return root

        root._get_height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # Left rotation
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z._get_height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y._get_height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z._get_height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y._get_height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def min_data_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    @time_logger
    def search(self, root, data):
        if not root or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)
