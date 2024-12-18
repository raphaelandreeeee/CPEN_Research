from .time_logger import time_logger


class BinarySearchTree:

    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __contains__(self, data) -> bool:
        if data not in self.inorder_traversal():
            return False
        return True

    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.data == other.data
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
            return self.data > other.data
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.data >= other.data
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.data < other.data
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.data <= other.data
        else:
            return NotImplemented
    
    def __repr__(self) -> str:
        return str(self.data)

    @time_logger
    def search(self, data) -> None:
        if self.data == data:
            return self
        elif self.data > data and self.left is not None:
            return self.left.search(data)
        elif self.data < data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    @time_logger
    def minimum(self) -> int:
        current = self.left

        while current is not None:
            if current.left is None:
                break
            current = current.left
        
        return current.data
    
    @time_logger
    def maximum(self) -> int:
        current = self.right

        while current is not None:
            if current.right is None:
                break
            current = current.right
        
        return current.data
    
    @time_logger
    def successor(self, data) -> int:
        if self.data == data:
            return self.right
        elif self.data < data and self.right is not None:
            return self.right.successor(data)

    @time_logger
    def predeccessor(self, data) -> int:
        if self.data == data:
            return self.left
        elif self.data > data and self.left is not None:
            return self.right.predeccessor(data)

    @time_logger
    def insert(self, data) -> None:
        if self.data is None:
            self.data = data
            return
        
        if self.data > data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    @time_logger
    def delete(self, data):
        if self is None:
            return self

        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # temp = self.right.minimum()
            # self.data = temp.data
            # self.right = self.right.delete(temp.data)

        return self

    def inorder_traversal(self) -> list:
        container = []

        if self.left is not None:
            container.extend(self.left.inorder_traversal())
        
        container.append(self.data)
        
        if self.right is not None:
            container.extend(self.right.inorder_traversal())

        return container
    
    def preorder_traversal(self) -> list:
        container = []

        container.append(self.data)
        
        if self.left is not None:
            container.extend(self.left.preorder_traversal())
        
        if self.right is not None:
            container.extend(self.right.preorder_traversal())

        return container

    def postorder_traversal(self) -> list:
        container = []

        if self.left is not None:
            container.extend(self.left.postorder_traversal())
        
        if self.right is not None:
            container.extend(self.right.postorder_traversal())

        container.append(self.data)
        
        return container
