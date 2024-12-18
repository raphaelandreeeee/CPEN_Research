# %% Array Complexity

from data_structures.my_array import Array
import sys
import json
import time
import matplotlib.pyplot as plt


with open(r"dataset_1.json", 'r') as file:
    file_data = json.load(file)

timeset_insert = []
timeset_search = []
timeset_delete = []
memoryset = []
sizes = []

count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    count += 1

    array = Array(4)

    start = time.perf_counter()
    array.insert(id_obj)
    array.insert(first_name + last_name)
    array.insert(attendance)
    timeset_insert.append(time.perf_counter() - start)

    memoryset.append(sys.getsizeof(array))

    start = time.perf_counter()
    array.search(0)
    timeset_search.append(time.perf_counter() - start)

    start = time.perf_counter()
    array.delete(0)
    timeset_delete.append(time.perf_counter() - start)

    sizes.append(count)

figure, axis = plt.subplots(2, 1)

axis[0].plot(sizes, timeset_insert, label='Insert Time', marker='o')
axis[0].plot(sizes, timeset_search, label='Search Time', marker='o')
axis[0].plot(sizes, timeset_delete, label="Delete Time", marker='o')
axis[0].set_title('Time and Space Complexity of Array')
axis[0].set_xlabel('Number of Operations')
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)

axis[1].plot(sizes, memoryset, label="Memory", marker='o')
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].legend()
axis[1].grid(True)

plt.show()


# %% Stack Complexity

from data_structures.my_stack import Stack
import matplotlib.pyplot as plt
import json
import sys
import time


with open(r"dataset_1.json", 'r') as file:
    file_data = json.load(file)

timeset_push = []
timeset_peek = []
timeset_pop = []
memoryset = []
sizes = []

count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    count += 1

    stack = Stack()

    start = time.perf_counter()
    stack.push(attendance)
    stack.push(first_name + last_name)
    stack.push(id_obj)
    timeset_push.append(time.perf_counter() - start)

    start = time.perf_counter()
    stack.peek()
    timeset_peek.append(time.perf_counter() - start)

    start = time.perf_counter()
    stack.pop()
    timeset_pop.append(time.perf_counter() - start)

    memoryset.append(sys.getsizeof(stack))

    sizes.append(count)

figure, axis = plt.subplots(2, 1)

axis[0].plot(sizes, timeset_push, label='Push Time', marker='o')
axis[0].plot(sizes, timeset_peek, label="Peek Time", marker='o')
axis[0].plot(sizes, timeset_pop, label="Peek Time", marker='o')
axis[0].set_title('Time and Space Complexity of Stack')
axis[0].set_xlabel("Per Instance")
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)

axis[1].plot(sizes, memoryset, label="Memory", marker='o')
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].legend()
axis[1].grid(True)

plt.show()

# %% Queue Complexity

from data_structures.my_queue import Queue
import matplotlib.pyplot as plt
import json
import sys
import time


with open(r"dataset_1.json", 'r') as file:
    file_data = json.load(file)

timeset_enqueue = []
timeset_peek = []
timeset_dequeue = []
memoryset = []
sizes = []

count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    count += 1

    queue = Queue()

    start = time.perf_counter()
    queue.enqueue(attendance)
    queue.enqueue(first_name + last_name)
    queue.enqueue(id_obj)
    timeset_enqueue.append(time.perf_counter() - start)

    start = time.perf_counter()
    queue.peek()
    timeset_peek.append(time.perf_counter() - start)

    start = time.perf_counter()
    queue.dequeue()
    timeset_dequeue.append(time.perf_counter() - start)

    memoryset.append(sys.getsizeof(stack))

    sizes.append(count)

figure, axis = plt.subplots(2, 1)

axis[0].plot(sizes, timeset_enqueue, label='Enqueue Time', marker='o')
axis[0].plot(sizes, timeset_peek, label="Peek Time", marker='o')
axis[0].plot(sizes, timeset_dequeue, label="Dequeue Time", marker='o')
axis[0].set_title('Time and Space Complexity of Queue')
axis[0].set_xlabel("Per Instance")
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)

axis[1].plot(sizes, memoryset, label="Memory", marker='o')
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].legend()
axis[1].grid(True)

plt.show()
# %%

from data_structures.my_linked_list import LinkedList
import matplotlib.pyplot as plt
import json
import sys
import time


with open(r"dataset_1.json", 'r') as file:
    file_data = json.load(file)

timeset_append = []
timeset_pop = []
memoryset = []
sizes = []

count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    count += 1

    ll = LinkedList()

    start = time.perf_counter()
    ll.append(attendance)
    ll.append(first_name + last_name)
    ll.append(id_obj)
    timeset_append.append(time.perf_counter() - start)

    memoryset.append(sys.getsizeof(ll))

    start = time.perf_counter()
    ll.pop(0)
    timeset_pop.append(time.perf_counter() - start)

    sizes.append(count)

figure, axis = plt.subplots(2, 1)

axis[0].plot(sizes, timeset_append, label='Append Time', marker='o')
axis[0].plot(sizes, timeset_pop, label="Pop Time", marker='o')
axis[0].set_title('Time and Space Complexity of Linked List')
axis[0].set_xlabel("Per Instance")
axis[0].set_ylabel('Time (seconds)')
axis[0].legend()
axis[0].grid(True)

axis[1].plot(sizes, memoryset, label="Memory", marker='o')
axis[1].set_xlabel("Per Instance")
axis[1].set_ylabel("Memory (Bytes)")
axis[1].legend()
axis[1].grid(True)

plt.show()

# %% Comparison

from data_structures.my_array import Array
from data_structures.my_stack import Stack
from data_structures.my_queue import Queue
from data_structures.my_linked_list import LinkedList
import sys
import json
import time
import matplotlib.pyplot as plt


with open(r"dataset_1.json") as file:
    file_data = json.load(file)


timeset_insert = []
timeset_search = []
timeset_delete = []
array_memoryset = []
 
timeset_push = []
timeset_peek_1 = []
timeset_pop_1 = []
stack_memoryset = []

timeset_enqueue = []
timeset_peek_2 = []
timeset_dequeue = []
queue_memoryset = []

timeset_append = []
timeset_pop_2 = []
linkedlist_memoryset = []

sizes = []

count = 0
for row in file_data:
    attendance, first_name, last_name, id_obj = row["attendance"], row["first_name"], row["last_name"], row["id"]

    count += 1
    sizes.append(count)

    # Array
    array = Array(4)

    start = time.perf_counter()
    array.insert(id_obj)
    array.insert(first_name + last_name)
    array.insert(attendance)
    timeset_insert.append(time.perf_counter() - start)

    array_memoryset.append(sys.getsizeof(array))

    start = time.perf_counter()
    array.search(0)
    timeset_search.append(time.perf_counter() - start)

    start = time.perf_counter()
    array.delete(0)
    timeset_delete.append(time.perf_counter() - start)

    # Stack
    stack = Stack()

    start = time.perf_counter()
    stack.push(attendance)
    stack.push(first_name + last_name)
    stack.push(id_obj)
    timeset_push.append(time.perf_counter() - start)

    start = time.perf_counter()
    stack.peek()
    timeset_peek_1.append(time.perf_counter() - start)

    start = time.perf_counter()
    stack.pop()
    timeset_pop_1.append(time.perf_counter() - start)

    stack_memoryset.append(sys.getsizeof(stack))

    # Queue
    queue = Queue()

    start = time.perf_counter()
    queue.enqueue(attendance)
    queue.enqueue(first_name + last_name)
    queue.enqueue(id_obj)
    timeset_enqueue.append(time.perf_counter() - start)

    start = time.perf_counter()
    queue.peek()
    timeset_peek_2.append(time.perf_counter() - start)

    start = time.perf_counter()
    queue.dequeue()
    timeset_dequeue.append(time.perf_counter() - start)

    queue_memoryset.append(sys.getsizeof(stack))

    # Linked List
    ll = LinkedList()

    start = time.perf_counter()
    ll.append(attendance)
    ll.append(first_name + last_name)
    ll.append(id_obj)
    timeset_append.append(time.perf_counter() - start)

    linkedlist_memoryset.append(sys.getsizeof(ll))

    start = time.perf_counter()
    ll.pop(0)
    timeset_pop_2.append(time.perf_counter() - start)

array_timesets = [sum(timeset_insert) / len(sizes), sum(timeset_search) / len(sizes), sum(timeset_delete) / len(sizes)]
array_memory = sum(array_memoryset) / len(sizes) 

stack_timesets = [sum(timeset_push) / len(sizes), sum(timeset_peek_1) / len(sizes), sum(timeset_pop_1) / len(sizes)]
stack_memory = sum(stack_memoryset) / len(sizes)

queue_timesets = [sum(timeset_enqueue) / len(sizes), sum(timeset_peek_2) / len(sizes), sum(timeset_dequeue) / len(sizes)]
queue_memory = sum(queue_memoryset) / len(sizes)

ll_timesets = [sum(timeset_append) / len(sizes), sum(timeset_pop_2) / len(sizes)]
ll_memory = sum(linkedlist_memoryset) / len(sizes)

figure, axis = plt.subplots(2, 1)

axis[0].set_title("Comparison of Data Structures' Time and Space Complexity")
axis[0].bar(["Insert(Array)", "Search(Array)", "Delete(Array)"], array_timesets, color='b', label="Array")
axis[0].bar(["Push(Stack)", "Peek(Stack)", "Pop(Stack)"], stack_timesets, color='g', label="Stack")
axis[0].bar(["Enqueue(Queue)", "Peek(Queue)", "Dequeue(Queue)"], queue_timesets, color='orange', label="Queue")
axis[0].bar(["Append(Linked List)", "Pop(Linked List)"], ll_timesets, color='yellow', label="Linked List")
axis[0].set_ylabel("Time Complexity (seconds)")
axis[0].set_xlabel("Operations")
axis[0].grid(True)
axis[0].set_axisbelow(True)

axis[1].bar(["Array", "Stack", "Queue", "Linked List"], array_memory + stack_memory + queue_memory + ll_memory, label="Memory Allocation")
axis[1].set_xlabel("Data Structures")
axis[1].set_ylabel("Memory (bytes)")
axis[1].grid(True)
axis[1].set_axisbelow(True)

plt.legend()
plt.show()


# %%
