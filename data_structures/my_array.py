from .time_logger import time_logger


class Array:

    def __init__(self, size):
        self.size = size
        self.container = []

    def __contains__(self, data):
        for value in self.container:
            if data == value:
                return True
        
        return False

    def __getitem__(self, index):
        return self.container[index]
    
    def __setitem__(self, index, value):
        self.container[index] = value

    def __repr__(self):
        return str(self.container)
    
    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] == self.container[0]
        else:
            return NotImplemented
        
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
        
    def __gt__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] > self.container[0]
        else:
            return NotImplemented
        
    def __ge__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] >= self.container[0]
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] < self.container[0]
        else:
            return NotImplemented
    
    def __le__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] <= self.container[0]
        else:
            return NotImplemented

    @time_logger
    def insert(self, data, index=None):
        if index is not None and index > len(self.container):
            raise IndexError("Index out of range")

        if index is None:
            self.container.append(data)
        else:
            self.container.insert(index, data)

    @time_logger
    def search(self, data):
        for i in range(self.size - 1):
            if self.container[i] == data:
                return i
    
    @time_logger
    def delete(self, index):
        if index > len(self.container):
            raise IndexError("Index out of range")

        del self.container[index]


if __name__ == '__main__':
    student = Array(2)

    student.insert(0)
    student.insert("rpahael")

    print(student.search("rpahael"))

    print(student)