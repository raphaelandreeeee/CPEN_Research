from .time_logger import time_logger


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return f"Node: {self.data}"


class Queue:

    def __init__(self) -> None:
        self.first = None
        self.size = 0

    def __len__(self) -> int:
        return self.size
    
    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.first == other.first
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
            return self.first > other.first
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.first >= other.first
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.first < other.first
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.first <= other.first
        else:
            return NotImplemented

    def __repr__(self) -> str:
        current = self.first
        container = ""

        while current:
            container = container + f"{current.data}, "
            if current.next_node is None:
                break
            current = current.next_node

        return f"[{container}]"

    @time_logger
    def enqueue(self, data) -> None:
        node = Node(data)
        self.size += 1

        if self.first is None:
            self.first = node
        else:
            current = self.first
            while current:
                if current.next_node is None:
                    break
                current = current.next_node
            current.next_node = node

    @time_logger
    def dequeue(self) -> None:
        current = self.first
        self.first = current.next_node
        current = None

        self.size -= 1

    @time_logger
    def peek(self):
        return self.first

    def is_empty(self) -> bool:
        return self.first is None
