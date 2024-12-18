import heaps
import sys
from my_array import Array


class MyHeap(heaps.Heap):
    def __init__(self):
        super().__init__()

    def __getitem__(self, index):
        return self.heap[index]


if __name__ == '__main__':
    container = MyHeap()

    student1 = Array(2)
    student2 = Array(2)
    student3 = Array(2)
    names = (name for name in ["raph", "james", "bill"])

    
    for student in [student1, student2, student3]:
        student.insert(0)
        student.insert(names.__next__())
        container.insert(student)

    print(container.heap[0][0])

    print(container)
    print(f"Space taken: {sys.getrefcount(container)}")
    print(container[0] == container[1])

    for student in container.heap:
        student[0] += 1
        break

    print(container)
    print(container[2] == container[1])
