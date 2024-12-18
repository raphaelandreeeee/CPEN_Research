from .time_logger import time_logger


class Heap:

    def __init__(self) -> None:
        self.heap = []
        self.size = 0
    
    def __repr__(self) -> str:
        return f"Heap: {self.heap}"

    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.heap[0] == other.heap[0]
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
            return self.heap[0] > other.heap[0]
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.heap[0] >= other.heap[0]
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.heap[0] < other.heap[0]
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.heap[0] <= other.heap[0]
        else:
            return NotImplemented

    def _get_parent_index(self, index) -> int:
        return index // 2
    
    def _get_left_child(self, index) -> int:
        return index * 2
    
    def _get_right_child(self, index) -> int:
        return (index * 2) + 1
    
    def _swap(self, index1, index2) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _heapify_up(self, index) -> None:
        parent = self._get_parent_index(index)

        while parent >= 0 and self.heap[parent] < self.heap[index]:
            self._swap(parent, index)
            index = parent
            parent = self._get_parent_index(index)

    def _heapify_down(self, index) -> None:
        left = self._get_left_child(index)
        right = self._get_right_child(index)

        minimum = index

        if left < len(self.heap) and self.heap[left] > self.heap[minimum]:
            self._swap(left, minimum)

        if right < len(self.heap) and self.heap[right] > self.heap[minimum]:
            self._swap(right, minimum)

        if minimum != index:
            self._swap(index, minimum)
            self._heapify_down(minimum)

    @time_logger
    def insert(self, data) -> None:
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)
        self.size += 1

    @time_logger
    def peek(self) -> int:
        if self.is_empty():
            return None
        
        return self.heap[0]
    
    @time_logger
    def delete(self) -> int:
        if self.is_empty():
            return None
        
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self._heapify_down(0)

        return maximum

    @time_logger
    def get_maximum(self) -> int:
        return self.heap[0]

    def is_empty(self) -> bool:
        return self.size == 0
