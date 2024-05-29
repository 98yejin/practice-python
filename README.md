# Practice Python 👩‍💻

## Contents

- Datastructures
- Algorithms
- Concurrent Programming
- Python Concurrency and Parallelism Problems
  - Concurrent Web Scraper
  - Parallel File Processing
  - Concurrent Producer-Consumer
- FAQs

## Datastructures

| index | datastructure | link                                 |
| ----- | ------------- | ------------------------------------ |
| 1     | Queue         | [link](/datastructure/_queue.py)     |
| 2     | Hashtable     | [link](/datastructure/hashtable.py)  |
| 3     | Linked list   | [link](/datastructure/linkedlist.py) |
| 4     | Stack         | [link](/datastructure/stack.py)      |
| 5     | Tree          | [link](/datastructure/tree.py)       |
| 6     | Minheap       | [link](/datastructure/minheap.py)    |
| 7     | trie          | [link](/datastructure/trie.py)       |
| 8     | merge sort    | [link](/datastructure/mergesort.py)  |

### Linked Lists

#### Singly Linked List

[Time Complexity]

- Accessing by index : O(m)
- Insertion/Deletion
- Head : O(1)
- Tail : O(n)
- Search: O(n)

[Space Complexity]

- One Node : O(1)
- Overall Node : O(n)

[When to use]

- Stacks, Queues
- Applications where memory efficiency is crucial.
- Situations where only forward traversal is required, such as parsing a linked list of data and processing it sequentially.

#### Doubly Linked List

[Time Complexity]

- Accessing by index : O(m)
- Insertion/Deletion
- Head : O(1)
- Tail : O(1)
- Search: O(n)

[Space Complexity]

- One Node : O(1)
- Overall Node : O(n)

[Why to use]

- Double linked list allow bidirectional traversal, which can be useful in certain scenarios, while single linked lists only support forward traversal.
- But consume more memory per node due to the additional reference to the previous node.

[When to use]

- Queues, deques, and hash tables
- Undo-redo functionality in text editors
- Applications where efficient insertion and deletion operations are required at both ends of the list
- Situations where bidirectional traversal is necessary, such as implementing a cursor in a text editor or navigating through a playlist in a media player

### Tree

- Interview Tip: Tree and graph problems often have ambiguous details or incorrect assumptions. Be cautious and, if necessary, ask for clarification.

[Traverse binary tree]

- In-order traversal (`L -> C -> R`)
- Pre-order traversal (`C -> L -> R`)
- Post-order traversal (`L -> R -> C`)

[Min-heap]

- A complete binary tree where the last level is filled from left to right.
- Each node's element is smaller than its children.
- Insert (`O(logn)`), extract_min (`O(logn)`)

[When to use]

- Searching
- Tree operations
- Expression evaluation
- Serialization/deserialization
- Tree visualization

### Tries

[Time Complexity]

- The time complexity of operations in a Trie depends primarily on the length of the keys and the number of keys stored in the Trie.
- For operations like insertion, search, deletion, and prefix search, the time complexity is typically O(m), where m is the length of the keys involved in the operation.

[When to use]

- Using a hash table, you can quickly determine whether a given string is valid or not, but you cannot determine if that string is a valid prefix of any valid word. By using a trie, you can quickly determine this.
- With a trie, you can check if a given string is a valid prefix in O(k) time, where k is the length of the string.
- This is the same time complexity as using a hash table.

[ETC]

- Also known as a prefix tree, a trie is a data structure that stores characters at each node, which is a variant of an N-ary tree.
- Traversing the tree downwards yields a single word.
- The null node, denoted by \*, often represents the end of a word.
- Widely used as a data structure for string search in natural language processing.
- Similar to building an index for each character.

### Graph

- A tree is a connected graph without cycles.
- A graph is a larger concept than a tree.
- A graph is simply a collection of nodes and the edges that connect those nodes.
- It can be directed or undirected.
- It may or may not have cycles, and a graph without cycles is called an acyclic graph.
- A graph can be composed of multiple isolated subgraphs, and a graph in which there is a path between every pair of vertices is called a connected graph.

[Graph Traversal]

- Depth-first search (preferred when visiting all nodes, must keep track of visited nodes to avoid infinite loops)
- Breadth-first search (used for finding shortest paths or arbitrary paths, uses a queue)

### Stack

[Time Complexity]

- empty() O(1)
- size(): O(1)
- top(), peek(): O(1)
- push(item): O1
- pop(): O(1)

[Why to use]

- Useful when using recursive algorithms.
- Follows LIFO (Last-In, First-Out) order.
- Suitable when you need to access the most recently added item first or when the order of processing needs to be reversed.

[When to use]

- Function Call Management
- Expression Evaluation
- Undo/Redo Operations
- Backtracking Algorithms ( Depth First Search )
- Parsing Algorithms like XML/HTML

### Queue

[Time Complexity]

- enqueue(item):O(1)
- dequeue(): O(1)
- peek(): O(1)
- isEmpty(): O(1)

Python’s collections.deque

- Copy O(n)
- Append, Append left O(1)
- Pop, Pop left O (1)
- Extend, extend left O(k)
- Rotate O(k)
- Remove O(n)
- Get Length O(1)

[Why to use]

- Suitable when you need to process items in the order they were added or when implementing systems with asynchronous tasks or requests.
- Queues are commonly used in systems with asynchronous tasks or requests, where tasks/requests arrive at irregular intervals and need to be processed in the order they were received. For example, in web servers, incoming HTTP requests are often placed in a queue and processed by worker threads in the order they were received.

[When to use]

- Job Scheduling
- Breadth First Search
- Buffering
- Print Queue Management
- Bounded Buffer

### Heapq ( priority queue )

[methods]

- heapq.heappush()
- heapq.heappop()
- heapq.heapify()
- heapq.nlargest()
- heapq.nsmallest()

[when to use]

- Heapsort
- Graph Algorithm
  (Dijkstra, Prim, A\*)
- File Compress
- Load Balancing

[ETC]

- Heaps are binary trees for which every parent node has a value less than or equal to any of its children. We refer to this condition as the heap invariant.
- heap[k] <= heap[2*k+1] or heap[k] <= heap[2\*k+2

### List

[Time Complexity]

- Copy O(n)
- Append O(1)
- Pop Last O(1)
- Pop intermediate O(n)
- Insert O(n)
- Get/Set Item O(1)
- Delete Item O(n)
- Iteration O(n)
- Get Slice O(k)
- Del Slice O(n)
- Set Slice O(k+n)
- Extend O(k)
- Sort O(nlogn)
- Multiply O(nk)
- x in s O(n)
- min(s): O(n)

[When to use]

- Dynamic memory allocation ( scenarios where the size of the data collection is not known in advance )
- Implementing stacks and queues

[Etc]

- Automatically resizes the size of the array.
- The size of the array or list increases every time data is appended.
- It maintains O(1) access time while being able to change the size as needed. Typically, when the array is full, the size is doubled. Doubling the size takes O(n) time, but it does not occur frequently, so when calculated as amortized insertion time, it is still O(1).

### Hash Table

[Time Complexity]

- K in d O(1) / O(n)
- Copy O(n) / O(n)
- get item O(1) / O(n)
- Set Item O(1) / O(n)
- Delete item O(1) / O(n)
- Iteration O(n) / O(n)

Avg case times listed for dict objects assume that hash function for the objects is sufficiently robust to make collisions uncommon

[Why to use]

- Efficient data structure for searching
- Can be implemented using linked lists and hash code function
- Alternatively, can be implemented using a balanced binary search tree. It uses potentially less space as it doesn't require pre-allocating a large array.
- Allows accessing the set of keys in a specific order

[When to use]

- Storing key-value pairs
- Database indexing
- Caching
- Symbol tables in compilers
- Implementing sets and bags
- Counting frequencies
- Hash-based algorithms

## Algorithms

| index | algorithm     | link                                |
| ----- | ------------- | ----------------------------------- |
| 1     | BFS           | [link](/algorithms/bfs.py)          |
| 2     | DFS           | [link](/algorithms/dfs.py)          |
| 3     | Binary Search | [link](/algorithms/binarysearch.py) |
| 4     | Quick Sort    | [link](/algorithms/quicksort.py)    |

### Breadth-First Search (BFS)

[Time Complexity]

O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

[Space Complexity]

O(V), where V is the number of vertices. In the worst case, the entire graph may need to be stored in the queue.

[When to use]

BFS is used to explore the vertices of a graph level by level, starting from a given source vertex. It is often used to find the shortest path in unweighted graphs, connected components, and more.

### Depth-First Search (DFS)

[Time Complexity]

O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. However, DFS can be faster in practice for some graph structures.

[Space Complexity]

O(V), where V is the number of vertices. In the worst case, the entire graph may need to be stored in the call stack.

[When to use]

DFS is used to explore the vertices of a graph deeply, following each branch until it reaches a dead end before backtracking. It is often used for topological sorting, cycle detection, maze solving, and more.

### Binary Search

[Time Complexity]

- O(log n), where n is the number of elements in the sorted array.
- if the array is not sorted, binary search cannot reliably find the target element. In such cases, alternative methods such as linear search (iterating through the array sequentially) may be used to find the target element, but with a time complexity of O(n) instead of O(log n) provided by binary search on a sorted array.

[Space Complexity]

O(1). Binary search is an in-place algorithm and does not require additional space.

[When to use]

Binary search is used to find the position of a target value within a sorted array efficiently. It repeatedly divides the search interval in half until the target value is found or the interval becomes empty.

### Merge Sort

[Time Complexity]

O(n log n), where n is the number of elements in the array.

[Space Complexity]

O(n), where n is the number of elements in the array. Merge sort requires additional space for merging subarrays during the merge step.

[How it works]

- Merge sort is a divide-and-conquer algorithm that recursively divides the array into smaller subarrays, sorts them independently, and then merges the sorted subarrays to produce the final sorted array.
- It is a stable sorting algorithm and is often used for sorting large datasets efficiently.

[Why to use]

- Efficiency: Merge sort has a time complexity of O(n log n) in all cases, making it efficient for sorting large datasets. Therefore, it is suitable for applications where sorting performance is important.
- Stability: Merge sort is a stable sorting algorithm, meaning it maintains the relative order of equal elements. This property is important in scenarios where the original order of equal elements needs to be preserved.
- Divide and conquer: Merge sort follows a divide and conquer strategy by recursively dividing the sorting problem into smaller subproblems, independently sorting them, and then merging the sorted subarrays. This makes it easier to implement and understand compared to other sorting algorithms.
- Predictable performance: Merge sort exhibits consistent performance characteristics and does not suffer from worst-case scenarios like some other sorting algorithms. It performs well on datasets of varying sizes and distributions.
- Not In-Place: Merge sort is not an in-place sorting algorithm and requires additional memory for merging subarrays. However, the efficiency and stability advantages often outweigh this overhead.

### Quick Sort

[Time Complexity]

O(n log n) on average, O(n^2) in the worst case, where n is the number of elements in the array.

[Space Complexity]

O(log n) on average, O(n) in the worst case due to recursive calls. Quick sort is an in-place sorting algorithm and does not require additional space for sorting.

[How it works]

- Quick sort is a divide-and-conquer algorithm that recursively partitions the array into smaller subarrays based on a pivot element, sorts the subarrays independently, and then combines them to produce the final sorted array.
- It is widely used in practice due to its efficiency on average and ease of implementation.

## Concurrent Programming

| index | concurrent programming  | link                                           |
| ----- | ----------------------- | ---------------------------------------------- |
| 1     | barriers                | [link](/concurrent/barriers.py)                |
| 2     | fizzbuzz                | [link](/concurrent/fizzbuzz.py)                |
| 3     | fizzbuzz_async          | [link](/concurrent/fizzbuzz_async.py)          |
| 4     | fizzbuzz_multithreading | [link](/concurrent/fizzbuzz_multithreading.py) |
| 5     | future                  | [link](/concurrent/future.py)                  |
| 6     | helloworld              | [link](/concurrent/helloworld.py)              |
| 7     | interface               | [link](/concurrent/interface.py)               |
| 8     | locks                   | [link](/concurrent/locks.py)                   |
| 9     | quickstart              | [link](/concurrent/quickstart.py)              |
| 10    | semaphores              | [link](/concurrent/semaphores.py)              |
| 11    | sharedresources         | [link](/concurrent/sharedresources.py)         |

### Common Concurrency Bugs

- Race Conditions: Occur when multiple threads access shared data concurrently, leading to unexpected behavior.
- Deadlocks: Happen when two or more threads are stuck waiting for each other to release resources, resulting in a deadlock.
- Livelocks: Similar to deadlocks, but threads are actively performing operations without making progress.
- Resource Leaks: Occur when resources (e.g., locks, semaphores) are not properly released, leading to resource exhaustion.

### Concurrency Concepts

- Parallelism vs. Concurrency:
  - Parallelism involves executing multiple tasks simultaneously on different processors or cores.
  - Concurrency involves managing and coordinating multiple tasks, which may or may not execute simultaneously.
- Processes and Threads:
  - Processes are separate instances of a program, each with its own memory space.
  - Threads are lightweight units of execution within a process, sharing the same memory space.
- Shared Resources and Synchronization:
  - Concurrent tasks often access shared resources, such as memory or files.
  - Synchronization mechanisms, like locks and semaphores, are used to coordinate access to shared resources and prevent race conditions.
- Communication and Coordination:
  - Concurrent tasks may need to communicate and coordinate with each other.
  - Inter-process communication (IPC) mechanisms, like pipes and message queues, enable communication between processes.
  - Inter-thread communication can be achieved through shared memory and synchronization primitives.

### Trade-offs

1. Complexity:
   - Concurrent programs are generally more complex to design, implement, and debug compared to sequential programs.
   - Coordinating and synchronizing concurrent tasks adds an additional layer of complexity.
2. Overhead:
   - Creating and managing concurrent units of execution (processes or threads) introduces overhead.
   - Context switching between tasks and synchronization operations can have performance implications.
3. Scalability:
   - Concurrency can improve the scalability of a program by allowing it to utilize available system resources effectively.
   - However, the scalability benefits may diminish if there are excessive synchronization or communication overheads.
4. Debugging and Testing:
   - Debugging concurrent programs can be challenging due to the non-deterministic nature of task interleaving.
   - Race conditions and deadlocks can be difficult to reproduce and diagnose.
   - Testing concurrent programs requires careful consideration of various interleaving scenarios.
5. Resource Utilization:
   - Concurrent programs can make efficient use of system resources, such as CPU cores and I/O devices.
   - However, excessive concurrency can lead to resource contention and decreased performance.
6. Synchronization Granularity:
   - Fine-grained synchronization (frequent locking) can minimize the time tasks spend waiting but introduces more overhead.
   - Coarse-grained synchronization (less frequent locking) reduces overhead but may lead to reduced concurrency.
7. Deadlocks and Livelocks:
   - Improper synchronization can result in deadlocks, where tasks are stuck waiting for each other indefinitely.
   - Livelocks occur when tasks are actively performing operations but unable to make progress.

### Processes, Threads, and the Global Interpreter Lock (GIL) in Python

- Processes:

  - Processes are separate instances of a program, each with its own memory space and system resources.
  - They provide true parallelism by running on separate CPU cores or even across multiple machines.
  - Processes have their own Python interpreter and do not share memory by default.
  - Communication between processes is done through inter-process communication (IPC) mechanisms like pipes, queues, or shared memory.

- Threads:
  - Threads are lightweight units of execution within a process.
  - They share the same memory space and can access the same global variables and data structures.
  - Threads are managed by the Python interpreter and are subject to the Global Interpreter Lock (GIL).
  - They are suitable for I/O-bound tasks or tasks that involve waiting for external resources.
- Global Interpreter Lock (GIL):
  - The GIL is a mutex that prevents multiple native threads from executing Python bytecodes simultaneously.
  - It ensures that only one thread can execute Python code at a time, even in a multi-threaded environment.
  - The GIL is necessary to protect the integrity of Python objects and manage memory safely.
  - It can limit the performance of CPU-bound tasks in multi-threaded Python programs.

### Differences between CPU-bound and I/O-bound tasks

- CPU-bound tasks:

  - These tasks are computationally intensive and spend most of their time utilizing the CPU.
  - Examples include complex calculations, data processing, or algorithmic operations.
  - CPU-bound tasks benefit from true parallelism, where multiple processes can execute on separate CPU cores simultaneously.
  - In Python, due to the GIL, multi-threading may not provide significant performance improvements for CPU-bound tasks.

- I/O-bound tasks:
  - These tasks spend most of their time waiting for input/output operations to complete.
  - Examples include reading from or writing to files, network communication, or interacting with databases.
  - I/O-bound tasks often involve blocking operations, where the program waits for the I/O operation to finish.
  - Multi-threading can be effective for I/O-bound tasks, as threads can perform other tasks while waiting for I/O operations to complete.

### Race Conditions, Deadlocks, and Synchronization Primitives

- Race Conditions:

  - A race condition occurs when multiple threads access shared data concurrently, and the final outcome depends on the relative timing of their execution.
  - It happens when threads perform non-atomic operations on shared data without proper synchronization.
  - Race conditions can lead to unpredictable and incorrect program behavior.
  - To prevent race conditions, synchronization mechanisms like locks or atomic operations should be used to ensure exclusive access to shared data.

- Deadlocks:
  - A deadlock is a situation where two or more threads are unable to proceed because each is waiting for the other to release a resource.
  - It occurs when there is a circular dependency between threads, and each thread is holding a resource that the other thread needs.
  - Deadlocks can result in a program becoming unresponsive or stuck indefinitely.
  - Techniques like resource ordering, timeout mechanisms, or deadlock detection algorithms can be used to prevent or recover from deadlocks.
- Synchronization Primitives:
  - Synchronization primitives are mechanisms used to coordinate the execution of concurrent threads and prevent race conditions and deadlocks.
  - Locks (mutexes) are used to ensure exclusive access to shared resources, allowing only one thread to execute a critical section at a time.
  - Semaphores are used to control access to a limited number of resources, allowing multiple threads to access the resources up to a specified limit.
  - Condition variables are used to synchronize threads based on a specific condition, allowing threads to wait until the condition is met.
  - Barriers are used to synchronize a group of threads, ensuring that all threads reach a certain point before proceeding further.

## Python Concurrency and Parallelism Problems

### [Concurrent Web Scraper](/crawler/)

- Objective: Implement a concurrent web scraper that retrieves data from
  multiple web pages simultaneously.
- Requirements:
  - Use the requests library to fetch web pages.
  - Utilize the asyncio module to achieve concurrency.
  - Scrape data from a list of URLs concurrently.
  - Process and store the scraped data.
- Extension: Implement rate limiting to avoid overloading the target website.

### [Parallel File Processing](/file_processing/)

- Objective: Develop a program that processes a large set of files concurrently.
- Requirements:
  - Accept a directory path as input.
  - Use the multiprocessing module to process files concurrently.
  - Apply a specific operation to each file (e.g., compression, encryption, or
    analysis).
  - Display the progress and status of the file processing.
- Extension: Implement error handling and logging for file processing failures.

### [Concurrent Producer-Consumer](/producer_consumer/)

- Objective: Implement a concurrent producer-consumer system using threads.
- Requirements:
  - Create a shared queue to store data items.
  - Implement producer threads that generate and add data items to the queue.
  - Implement consumer threads that retrieve and process data items from the
    queue.
  - Use synchronization primitives (e.g., locks or semaphores) to ensure thread
    safety.
  - Display the production and consumption of data items.
- Extension: Implement a mechanism to gracefully terminate the producer and
  consumer threads.

## FAQs

### Memory - Heap vs Stack

#### Memory - Stack

- Automatic Memory Management: The stack is managed automatically by the compiler or runtime environment. Memory allocated on the stack is automatically deallocated when it goes out of scope.
- Static Memory Allocation: Memory allocation on the stack follows a Last-In-First-Out (LIFO) strategy. Each function call creates a new stack frame, which includes parameters, local variables, and return addresses.
  Limited Size: The stack has a fixed and limited size, typically smaller than the heap. This size is determined at compile time or by system settings.
- Faster Access: Accessing memory on the stack is faster than on the heap because it involves simple pointer arithmetic.
- Scope-based: Variables allocated on the stack have a limited scope and are only accessible within the block or function in which they are declared.

#### Memory - Heap

- Manual Memory Management: Memory on the heap is managed manually by the programmer. Memory allocated on the heap must be explicitly deallocated to prevent memory leaks.
- Dynamic Memory Allocation: Memory allocation on the heap can be dynamic, allowing for flexible memory usage and allocation of memory blocks of varying sizes.
- Unlimited Size: The heap typically has a larger and theoretically unlimited size compared to the stack. However, it can be limited by available system resources.
- Slower Access: Accessing memory on the heap involves dereferencing pointers, which can be slower than accessing memory on the stack.
- Global Scope: Memory allocated on the heap can have a global scope and can be accessed from anywhere in the program.
  Potential for Memory Fragmentation: Memory fragmentation can occur on the heap over time, leading to inefficient memory usage and potential allocation failures.
- Choosing Between Stack and Heap:
  Lifetime of Data: Use the stack for data with a short lifetime, such as function parameters and local variables. Use the heap for data with a longer lifetime or dynamic memory requirements.
- Scope: Use the stack for variables with a limited scope and predictable lifetime. Use the heap for variables with a broader scope or lifetime extending beyond the current scope.
- Size Consideration: Consider the size of data when choosing between the stack and heap. Large data structures may exceed the stack's size limit and should be allocated on the heap.

In summary, the stack and heap serve different purposes in memory management, with the stack providing automatic and scoped memory allocation, while the heap offers manual and dynamic memory allocation. The choice between stack and heap depends on factors such as data lifetime, scope, and memory requirements.

### Recursion vs Iteration

- Using recursive algorithms can lead to poor space efficiency. Each recursive call adds a new layer to the stack, which means that O(n) memory is used when the depth of recursion is n.
- For this reason, it may be better to implement recursive algorithms iteratively. However, code implemented iteratively can sometimes be much more complex, so it may be better to compromise.
- By default, the number of recursive calls in Python is set to 1000. It is possible to change this value, but be cautious as it may lead to a recursion error and cause the stack to overflow. In such cases, using an iterative approach can be an alternative solution.

### Process vs Thread

- A process can be thought of as an instance of an executing program. It is an independent entity that is allocated system resources such as CPU time and memory. Each process runs in a separate address space and cannot access the variables or data structures of other processes. If one process needs to access the resources of another process, inter-process communication (IPC) must be used. IPC methods include pipes, files, and sockets.

- Threads exist within a process and share the process's resources, such as the heap space. Multiple threads within the same process share the same heap space. However, a process cannot directly access the memory of another process. Each thread has its own registers and stack, but they can read and write to the shared heap memory.

- Threads are like specific execution paths within a process. When one thread modifies the resources of a process, other sibling threads can immediately see the changes.

### Context Switching

Context Switching is the time it takes to switch between two processes. It refers to the time it takes to transition a waiting process to the running state and to transition a running process to the waiting or terminated state. This occurs during multitasking. The operating system needs to load the state information of the waiting process into memory and save the state information of the currently running process.

### Deadlock

[Conditions for Deadlock]

- Mutual Exclusion: Only one process can use a shared resource at a time.
- Hold and Wait: A process holding a resource can request additional resources without releasing the ones it already holds.
- No Preemption: Resources cannot be forcibly taken away from a process.
- Circular Wait: There is a circular chain of two or more processes, where each process is waiting for a resource held by another process in the chain.

Since it is difficult to release Mutual Exclusion for most shared resources, the focus is on preventing Circular Wait.

### Synchroneous vs Asynchroneous

Unless there is I/O involved, synchronous functions are much faster due to the Global Interpreter Lock (GIL).

- Function Calls and Overhead

  - Synchronous Functions: Synchronous functions have a direct and simple call stack. Each function is executed until completion when called, without any context switching to other tasks. This is highly efficient and eliminates unnecessary delays in the execution of tasks.
  - Asynchronous Functions: Asynchronous functions, such as asyncio, schedule and execute tasks using an event loop. This process involves additional steps such as function calls, task preparation, registering tasks with the event loop, and waiting for completion. Each of these steps incurs overhead, which can have an impact on the overall execution time, especially in CPU-bound tasks.

- Nature of the Task

  - CPU-Bound Tasks: Problems like FizzBuzz involve calculating numbers and evaluating conditions, which are CPU-bound tasks. In such tasks, continuous and fast processing is important. Synchronous processing methods that can handle tasks quickly may be more suitable for CPU-bound tasks.
  - I/O-Bound Tasks: Asynchronous functions are effective in handling I/O tasks (e.g., file reading/writing, network requests). I/O tasks have long waiting times, so the event loop can perform other tasks while waiting for the completion of I/O tasks, making efficient use of resources.

- Suitability of Asynchronous Programming
  - Suitability of Asynchronous Programming: Asynchronous programming is designed to optimize inherently inefficient I/O tasks. Therefore, applying asynchronous programming to simple computational tasks that are not I/O-bound can be overkill and may even degrade performance.

In the end, the choice of technology should always be based on the nature of the problem. For CPU-bound tasks like FizzBuzz, traditional synchronous processing methods may be more efficient in terms of performance. Asynchronous programming primarily demonstrates its advantages in I/O-bound tasks, so it is important to understand the nature of the task and choose the appropriate tool.

### 파이썬의 라이프사이클 관리

- Program Execution

  - Source Code Interpretation: When a Python program starts, the Python interpreter first reads the source code. This code can be in the form of a text file (.py) or already compiled bytecode (.pyc).
  - Compilation: The source code is then compiled into bytecode by the built-in Python compiler. This bytecode is an intermediate form of code that the Python Virtual Machine (PVM) can understand.
  - Execution: The compiled bytecode is executed by the Python Virtual Machine. The PVM is a stack-based interpreter that processes each operation sequentially.

- Memory Management and Garbage Collection

  - Automatic Memory Management: Python provides automatic memory management. Developers can focus on object creation, and the memory allocation for created objects is handled automatically by the Python interpreter.
  - Reference Counting: Python tracks the number of references to an object and releases the object from memory when the reference count reaches 0. This is the most basic memory management technique.
  - Garbage Collection: To address cyclic reference problems that cannot be solved by reference counting alone, Python includes a garbage collector. It periodically scans the memory to find and release objects that are no longer reachable.
  - Generational Collection: Python uses generational garbage collection algorithm. It divides objects into multiple generations based on how long they have been created. Garbage from younger generations is collected more frequently, while older generations are collected less frequently. This method optimizes memory management efficiency.

- Termination Handling
  - Cleanup: When a program is terminated, the Python interpreter performs cleanup tasks such as closing open file handles, terminating network connections, and releasing all system resources allocated to the process.
  - Returning Exit Code: The Python interpreter returns an exit code to the operating system to indicate whether the program terminated successfully or due to an error.
