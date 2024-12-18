from .time_logger import time_logger

class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return f"Node: {self.data}"


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.next = None
        self.size = 0
        
    def __repr__(self) -> str:
        current = self.top
        container = ""

        while current:
            container = f"{current.data}, " + container
            if current.next_node is None:
                break
            current = current.next_node

        return f"[{container}]"

    def __len__(self) -> int:
        return self.size
    
    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.top == other.top
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
            return self.top > other.top
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.top >= other.top
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.top < other.top
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.top <= other.top
        else:
            return NotImplemented

    @time_logger
    def push(self, data) -> None:
        node = Node(data)
        self.size += 1

        if self.top is None:
            self.top = node
        else:
            node.next_node = self.top
            self.top = node

    @time_logger
    def pop(self) -> any:
        item = self.top
        new_top = item.next_node
        self.top = new_top

        self.size -= 1

        return item.data

    @time_logger
    def peek(self) -> any:
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    print(stack)

    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(stack)

    item = stack.pop()
    print(stack, item)

    print(stack.peek())

    print(stack.__len__())
