# %%

from data_structures.my_array import Array
import json


with open(r"dataset_1.json", "r") as file:
    file_data = json.load(file)

new_file_data = [Array(4) for _ in enumerate(file_data)]
count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    new_file_data[count].insert(attendance)
    new_file_data[count].insert(first_name)
    new_file_data[count].insert(last_name)
    new_file_data[count].insert(id_obj)

    count += 1

test = new_file_data[99]

# %%% Array Complexity
from data_structures.my_array import Array
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

array = Array(sizes)

timeset_insert_1 = []
for row in new_file_data:
    start = time.perf_counter()
    array.insert(row)
    timeset_insert_1.append(time.perf_counter() - start)

start = time.perf_counter()
array.search(test)
timeset_search_1 = time.perf_counter() - start

start = time.perf_counter()
array.delete(99)
timeset_delete_1 = time.perf_counter() - start

array_memoryset = sys.getsizeof(array)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Insert"], sum(timeset_insert_1) / len(new_file_data), label='Insert Time',)
axis[0].bar(["Search"], timeset_search_1, label='Search Time',)
axis[0].bar(["Delete"], timeset_delete_1, label="Delete Time",)
axis[0].set_title('Time and Space Complexity of Array')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", array_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()


# %%% Stack Complexity

from data_structures.my_stack import Stack
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

stack = Stack()

timeset_push = []
for row in new_file_data:
    start = time.perf_counter()
    stack.push(row)
    timeset_push.append(time.perf_counter() - start)

start = time.perf_counter()
stack.peek()
timeset_peek_1 = time.perf_counter() - start

start = time.perf_counter()
stack.pop()
timeset_pop = time.perf_counter() - start

stack_memoryset = sys.getsizeof(stack)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Push"], sum(timeset_push) / len(new_file_data), label='Push Time',)
axis[0].bar(["Peek"], timeset_peek_1, label='Peek Time',)
axis[0].bar(["Pop"], timeset_pop, label="Pop Time",)
axis[0].set_title('Time and Space Complexity of Stack')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", stack_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()

# %%% Queue Complexity

from data_structures.my_queue import Queue
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

queue = Queue()

timeset_enqueue = []
for row in new_file_data:
    start = time.perf_counter()
    queue.enqueue(row)
    timeset_enqueue.append(time.perf_counter() - start)

start = time.perf_counter()
queue.peek()
timeset_peek_2 = time.perf_counter() - start

start = time.perf_counter()
queue.dequeue()
timeset_dequeue = time.perf_counter() - start

queue_memoryset = sys.getsizeof(queue)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Enqueue"], sum(timeset_enqueue) / len(new_file_data), label='Enqueue Time',)
axis[0].bar(["Peek"], timeset_peek_2, label='Peek Time',)
axis[0].bar(["Dequeue"], timeset_dequeue, label="Dequeue Time",)
axis[0].set_title('Time and Space Complexity of Queue')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", queue_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()

# %%% Linked List Complexity

from data_structures.my_linked_list import LinkedList
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

ll = LinkedList()

timeset_append = []
for row in new_file_data:
    start = time.perf_counter()
    ll.append(row)
    timeset_append.append(time.perf_counter() - start)

start = time.perf_counter()
ll.search(test)
timeset_search_2 = time.perf_counter() - start

start = time.perf_counter()
ll.delete(test)
timeset_delete_2 = time.perf_counter() - start

ll_memoryset = sys.getsizeof(ll)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Append"], sum(timeset_append) / len(new_file_data), label='Append Time',)
axis[0].bar(["Search"], timeset_search_2, label='Search Time',)
axis[0].bar(["Delete"], timeset_delete_2, label='Delete Time',)
axis[0].set_title('Time and Space Complexity of Linked List')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", ll_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()

# %%% Binary Search Tree Complexity

from data_structures.my_bst import BinarySearchTree
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

bst = BinarySearchTree()

timeset_insert_2 = []
for row in new_file_data:
    start = time.perf_counter()
    bst.insert(row)
    timeset_insert_2.append(time.perf_counter() - start)

start = time.perf_counter()
bst.search(test)
timeset_search_3 = time.perf_counter() - start

start = time.perf_counter()
bst.delete(test)
timeset_delete_3 = time.perf_counter() - start

bst_memoryset = sys.getsizeof(bst)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Insert"], sum(timeset_insert_2) / len(new_file_data), label='Insert Time')
axis[0].bar(["Search"], timeset_search_3, label="Search Time")
axis[0].bar(["Delete"], timeset_delete_3, label="Delete Time")
axis[0].set_title('Time and Space Complexity of Binary Search Tree')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", bst_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()

# %%% Heap Complexity

from data_structures.my_heap import Heap
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

heap = Heap()

timeset_insert_3 = []
for row in new_file_data:
    start = time.perf_counter()
    heap.insert(row)
    timeset_insert_3.append(time.perf_counter() - start)

start = time.perf_counter()
heap.peek()
timeset_peek_3 = time.perf_counter() - start

start = time.perf_counter()
heap.delete()
timeset_delete_4 = time.perf_counter() - start

heap_memoryset = sys.getsizeof(heap)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Insert"], sum(timeset_insert_3) / len(new_file_data), label='Insert Time')
axis[0].bar(["Peek"], timeset_peek_3, label="Peek Time")
axis[0].bar(["Delete"], timeset_delete_4, label="Delete Time")
axis[0].set_title('Time and Space Complexity of Heap')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", heap_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()


# %%% Hash Table Complexity

from data_structures.my_hash_table import HashTable
import matplotlib.pyplot as plt
import time
import sys

sizes = len(new_file_data)

ht = HashTable(sizes)

timeset_insert_4 = []
count = 0
for row in new_file_data:
    start = time.perf_counter()
    ht.insert(count, row)
    timeset_insert_4.append(time.perf_counter() - start)
    count += 1

start = time.perf_counter()
ht.search(99)
timeset_search_4 = time.perf_counter() - start

start = time.perf_counter()
ht.delete(99)
timeset_delete_5 = time.perf_counter() - start

ht_memoryset = sys.getsizeof(ht)

figure, axis = plt.subplots(2, 1)

axis[0].bar(["Insert"], sum(timeset_insert_4) / len(new_file_data), label='Insert Time')
axis[0].bar(["Search"], timeset_search_4, label="Search Time")
axis[0].bar(["Delete"], timeset_delete_5, label="Delete Time")
axis[0].set_title('Time and Space Complexity of Hash Table')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar("Memory", ht_memoryset, label="Memory")
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].set_xlim(-2, 2)
axis[1].legend()
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.show()


# %%% Comparison 

import numpy as np

offset = np.arange(7)
barWidth = 0.25

operations_1 = [sum(timeset_insert_1) / len(new_file_data), sum(timeset_push) / len(new_file_data), sum(timeset_enqueue) / len(new_file_data), sum(timeset_append) / len(new_file_data), sum(timeset_insert_2) / len(new_file_data), sum(timeset_insert_3) / len(new_file_data), sum(timeset_insert_4) / len(new_file_data)]
operations_2 = [timeset_search_1, timeset_peek_1, timeset_peek_2, timeset_search_2, timeset_search_3, timeset_peek_3, timeset_search_4]
operations_3 = [timeset_delete_1, timeset_pop, timeset_dequeue, timeset_delete_2, timeset_delete_3, timeset_delete_4, timeset_delete_5]

figure, axis = plt.subplots(1, 1)

plt.bar(offset - barWidth, operations_1, label="Insert Time", width=barWidth)
plt.bar(offset, operations_2, label="Search Time", width=barWidth)
plt.bar(offset + barWidth, operations_3, label="Delete Time", width=barWidth)
plt.xlabel("Data Structure")
plt.ylabel("Time (seconds)")
plt.xticks(offset, ["Array", "Stack", "Queue", "Linked List", "BST", "Heap", "Hash Table"])
plt.title("Comparison of Time Complexity of Data Structures")
plt.legend()
axis.grid(True)
axis.set_axisbelow(True)

plt.show()

# %%% Comparison 2

figure, axis = plt.subplots(1, 1)

plt.bar(["Array", "Stack", "Queue", "Linked List", "BST", "Heap", "Hash Table"], [array_memoryset, stack_memoryset, queue_memoryset, ll_memoryset, bst_memoryset, heap_memoryset, ht_memoryset])
plt.xlabel("Data Structure")
plt.ylabel("Memory (Bytes)")
plt.title("Comparison of Memory Complexity of Data Structures")
plt.ylim(0, 100)
axis.grid(True)
axis.set_axisbelow(True)
plt.show()
