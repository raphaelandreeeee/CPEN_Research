from .time_logger import time_logger


class Node:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return f"Node: {self.data}"


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __contains__(self, data) -> bool:
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next_node
        return False

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        l = []
        current = self.head

        if current.next_node is None:
            return f"Head: {current.data}"

        while current is not None:
            if current == self.head:
                l.append(f"Head: {current.data}")
            elif current.next_node is None:
                l.append(f"Tail: {current.data}")
                break
            else:
                l.append(f"{current}")
            current = current.next_node

        return "-> ".join(l)

    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.head == other.head
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
            return self.head > other.head
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.head >= other.head
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.head < other.head
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.head <= other.head
        else:
            return NotImplemented

    @time_logger
    def append(self, data) -> None:
        node = Node(data)
        self.size += 1

        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node

    @time_logger
    def prepend(self, data) -> None:
        node = Node(data)
        self.size += 1

        node.next_node = self.head
        self.head = node

    @time_logger
    def insert(self, index, data) -> None:
        current = self.head
        self.size += 1

        if index == 0:
            self.prepend(data)
        else:
            node = Node(data)
            for i in range(index - 1):
                current = current.next_node

            if current is None:
                raise IndexError("Index out of bounds.")
            else:
                node.next_node = current.next_node
                current.next_node = node

    @time_logger
    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current
            current = current.next_node

        return None

    @time_logger
    def delete(self, data) -> None:
        current = self.head
        self.size -= 1

        if current.data == data:
            self.head = current.next_node
            current = None
        else:
            while current.next_node:
                if current.next_node.data == data:
                    current.next_node = current.next_node.next_node
                    break
                current = current.next_node

    @time_logger
    def pop(self, index) -> None:
        if self.head is None:
            raise IndexError("Index out of bounds.")
        else:
            current = self.head
            self.size -= 1

        if index == 0:
            self.head = current.next_node
            current = None
        else:
            for i in range(index - 1):
                if current.next_node is None:
                    raise IndexError("Index out of bounds.")
                current = current.next_node

            if current.next_node is None:
                raise IndexError("Index out of bounds.")
            else:
                current.next_node = current.next_node.next_node
