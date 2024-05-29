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

- interview tip : 트리 및 그래프 문제들은 대부분 세부사항이 모호하거나 가정 자체가 틀린 경우가 많다. 유의하고, 필요하다면 명확하게 해 줄 것을 요구하자.

[Traverse binary tree]

- In-order traversal ( `L -> C -> R` )
- Pre-order-traversal ( `C -> L -> R` )
- Post-order traversal ( `L -> R -> C` )

[Min-heap]

- 트리의 마지막 단계에서 오른쪽 부분을 뺀 부분이 가득 채워졌다는 점이 완전 이진 트리
- 각 노드의 원소가 자식보다 작다는 특성이 있음
- Insert( `O( logn)` ), extract_min ( `O( logn)` )

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

- 해시테이블을 이용하면 주어진 문자열이 유효한지 아닌지 빠르게 확인할 수 있지만, 그 문자열이 어떤 유효한 단어의 접두사인지 확인할 수는 없다. 트라이를 이용하면 아주 빠르게 확인할 수 있다.
- 트라이는 길이가 k인 문자열이 주어졌을 때 O(k) 시간에 해당 문자열이 유효한 접두사인지 확인할 수 있다.
- 해시테이블을 사용했을 때와 같은 수행 시간이다.

[ETC]

- Prefix tree 라고도 불리는 trie
- N-ary tree 의 변종으로 각 노드에 문자를 저장하는 자료구조
- 트리를 아래쪽으로 순회하면 단어 하나가 나옴
- 널 노드라고 불리는 \* 노드는 종종 단어의 끝을 나타냄
- 자연어 처리 분야에서 문자열 탐색을 위한 자료구조로 널리 쓰임
- 각각의 문자 단위로 색인을 구축한 것과 유사

### Graph

- 트리는 사이클이 없는 하나의 연결 그래프임.
- 그래프가 트리보다 큰 개념임.
- 그래프는 단순히 노드와 그 노드를 연결하는 간선(edge)을 하나로 모아놓은 것임
- 방향성이 있을 수도 있고 없을 수도 있음.
- 사이클이 존재하지 않을 수도 있고 acycle graph 라고 부름
- 그래프는 여러개의 고립된 부분 그래프(isolated subgraphs)로 구성될 수 있고, 모든 정점 쌍(pair of vertices) 간에 경로가 존재하는 그래프는 연결 그래프라고 부름.

[그래프 탐색]

- Depth-first search ( 모든 노드를 방문하고자 할 때 선호됨, 반드시 어떤 노드를 방문했는지 체크해야함. 안그러면 무한루프 빠지기 쉬움 )
- Breadth-first search ( 최단 경로 또는 임의의 경로, Queue 사용 )

### Stack

[Time Complexity]

- empty() O(1)
- size(): O(1)
- top(), peek(): O(1)
- push(item): O1
- pop(): O(1)

[Why to use]

- 재귀 알고리즘을 사용할 때 유용하다.
- LIFO 순서를 따른다.
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

- 배열의 크기를 자동으로 조절할 수 있음.
- 데이터를 덧붙일 때마다 배열 혹은 리스트의 크기가 증가함.
- 필요에 따라 크기를 변화시킬 수 있으면서도 O(1)의 접근 시간을 유지함. 통상적으로 배열이 가득 차는 순간, 배열의 크기를 두 배로 늘림. 크기를 두 배 늘리는 시간은 O(n)이지만 자주 발생하는 일이 아니어서 amortized insertion time 으로 계산했을 때는 여전히 O(1) 임

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

- 효율적인 탐색을 위한 자료구조
- Linked list 와 hash code function 으로 구현할 수 있음
- 또는 균형 이진 탐색 트리로 구현할 수 있음. 크기가 큰 배열을 미리 할당해 놓지 않아도 되기 때문에 잠재적으로 적은 공간을 사용함.
- 키의집합을 특정 순서대로 접근할 수 있음

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

- 효율성 : 병합 정렬은 모든 경우에 O(n log n)의 시간 복잡도를 가지므로 대규모 데이터 세트를 정렬하는 데 효율적입니다. 따라서 정렬 성능이 중요한 응용 분야에 적합합니다.
- 안정성 : 병합 정렬은 안정적인 정렬 알고리즘입니다. 즉, 동일한 요소의 상대적 순서를 유지합니다. 이 속성은 동일한 요소의 원래 순서를 유지해야 하는 시나리오에서 중요합니다.
- 분할 정복 : 병합 정렬은 정렬 문제를 더 작은 하위 문제로 나누고 독립적으로 정렬한 다음 정렬된 하위 배열을 병합하는 분할 정복 전략을 따릅니다. 이는 다른 정렬 알고리즘에 비해 구현하고 이해하기가 더 쉽습니다.
- 예측 가능한 성능 : 병합 정렬은 일관된 성능 특성을 가지며 다른 정렬 알고리즘과 같이 최악의 시나리오를 겪지 않습니다. 다양한 크기와 분포를 가진 데이터 세트에서도 잘 작동합니다.
- 내부 아님(Not In-Place) : 병합 정렬은 내부 정렬 알고리즘이 아니며 하위 배열 병합을 위해 추가 메모리가 필요하지만 효율성과 안정성 이점이 이 오버헤드보다 더 큰 경우가 많습니다.

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

#### Stack

- Automatic Memory Management: The stack is managed automatically by the compiler or runtime environment. Memory allocated on the stack is automatically deallocated when it goes out of scope.
- Static Memory Allocation: Memory allocation on the stack follows a Last-In-First-Out (LIFO) strategy. Each function call creates a new stack frame, which includes parameters, local variables, and return addresses.
  Limited Size: The stack has a fixed and limited size, typically smaller than the heap. This size is determined at compile time or by system settings.
- Faster Access: Accessing memory on the stack is faster than on the heap because it involves simple pointer arithmetic.
- Scope-based: Variables allocated on the stack have a limited scope and are only accessible within the block or function in which they are declared.

#### Heap

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

재귀적 알고리즘을 사용하면 공간 효율성이 나빠질 수 있다. 재귀 호출이 한 번 발생할 때마다 스택에 새로운 층(layer)을 추가해야 한다. 이는 재귀의 깊이가 n일 때 O(n) 만큼의 메모리를 사용하게 된다는 것을 의미한다.
이런 이유로 재귀적 알고리즘을 순환적으로 구현하는 게 더 나을 수도 있다. 하지만 순환적으로 구현된 코드는 때로는 훨씬 더 복잡하기 때문에 타협하는 게 나을 수 있다.

```
python recursive 횟수 기본적으로 1000번으로 설정되어 있음. 변경은 가능하지만, recursion error 가 발생해서 스택이 터질 수 있고 이런 경우 iterative approach 를 사용하는 것도 방법임
```

### Process vs Thread

- 프로세스는 실행되고 있는 프로그램의 인스턴스라고 생각할 수 있다. 프로세스는 CPU 시간이나 메모리 등의 시스템 자원이 할당되는 독립적인 객체이다. 각 프로세스는 별도의 주소 공간에서 실행되며, 한 프로세스는 다른 프로세스의 변수나 자료구조에 접근할 수 없다. 한 프로세스가 다른 프로세스의 자원에 접근하려면 프로세스 간 통신(IPC, inter-process communication)을 사용해야 한다. 프로세스 간 통신 방법으로는 파이프, 파일, 소켓(pipes, queues, or shared memory) 등을 이용한 방법이 있다.

- 스레드는 프로세스 안에 존재하며 프로세스의 자원(힙 공간 등)을 공유한다. 같은 프로세스 안에 있는 여러 스레드들은 같은 힙 공간을 공유한다. 반면에 프로세스는 다른 프로세스의 메모리에 직접 접근할 수 없다. 각각의 스레드는 별도의 레지스터와 스택을 갖고 있지만, 힙 메모리는 서로 읽고 쓸 수 있다.

- 스레드는 프로세스의 특정한 수행 경로와 같다. 한 스레드가 프로세스 자원을 변경하면, 다른 이웃 스레드(sibling thread)도 그 변경 결과를 즉시 볼 수 있다.

### Context Switching

Context Switching 은 두 프로세스를 전환하는 데 드는 시간이다. 즉, 대기 중인 프로세스를 실행 상태로 전환하고, 실행 중인 프로세스를 대기 상태나 종료 상태로 전환하는 데 드는 시간이다. 멀티태스킹을 할 때 이런 일이 발생한다. 운영체제는 대기중인 프로세스의 상태 정보를 메모리에 올리고, 현재 실행 중인 프로세스의 상태 정보는 저장해야 한다.

### Deadlock

[발생 조건]

- Mutual Exclusion: 한번에 한 프로세스만 공유 자원을 사용할 수 있다.
- Hold and Wait: 공유 자원에 대한 접근 권한을 갖고 있는 프로세스가, 그 접근 권한을 양보하지 않은 상태에서 다른 자원에 대한 접근 권한을 요구할 수 있다
- No Preemption: 한 프로세스가 다른 프로세스의 자원 접근 권한을 강제로 취소할 수 없다
- Circular wait: 두 개 이상의 프로세스가 자원 접근을 기다리는데, 그 관계에 사이클이 존재한다

공유 자원 중 많은 경우 Mutual Exclusion 은 해제하기 어렵기 때문에, Circular Wait 을 방지하는 데 초점이 맞춰져 있다.

### Synchroneous vs Asynchroneous

I/O 작업이 없는 이상 GIL 때문에 동기 함수가 훨씬 빠르다.

- 함수 호출과 오버헤드

  - 동기 함수: 동기 함수는 직접적이고 단순한 호출 스택을 가집니다. 각 함수는 호출되면 완료될 때까지 실행되며, 다른 작업으로의 컨텍스트 전환은 발생하지 않습니다. 이는 매우 효율적이며, 작업의 불필요한 지연이 없습니다.
  - 비동기 함수: asyncio와 같은 비동기 함수는 이벤트 루프를 사용하여 작업을 스케줄링하고 실행합니다. 이 과정에서 함수 호출, 작업 준비, 이벤트 루프에 작업을 등록하고, 완료를 기다리는 등의 추가적인 스텝이 필요합니다. 이러한 각 스텝은 오버헤드를 발생시키며, 특히 CPU 바운드 작업에서는 이 오버헤드가 전체 실행 시간에 영향을 줄 수 있습니다.

- 작업의 본질

  - CPU 바운드 작업: FizzBuzz와 같은 문제는 숫자를 계산하고 조건을 평가하는 CPU 바운드 작업입니다. 이러한 작업에서는 연속적이고 빠른 처리가 중요합니다. CPU 바운드 작업에서는 작업을 빠르게 처리할 수 있는 동기 처리 방식이 더 적합할 수 있습니다.
  - I/O 바운드 작업: 비동기 함수는 I/O 작업(예: 파일 읽기/쓰기, 네트워크 요청)을 처리할 때 효과적입니다. I/O 작업은 대기 시간이 길기 때문에, 이벤트 루프는 I/O 작업이 완료되기를 기다리는 동안 다른 작업을 진행할 수 있어 자원을 효율적으로 사용할 수 있습니다.

- 비동기 프로그래밍의 적합성
  - 비동기 프로그래밍의 적합성: 비동기 프로그래밍은 본질적으로 비효율적인 I/O 작업을 최적화하도록 설계되었습니다. 따라서 I/O 바운드가 아닌 간단한 계산 작업에 비동기 프로그래밍을 적용하는 것은 오버킬일 수 있으며, 오히려 성능을 저하시킬 수 있습니다.

결국, 기술 선택은 항상 문제의 특성에 맞추어 결정되어야 합니다. FizzBuzz와 같은 CPU 바운드 작업에서는 전통적인 동기 처리 방식이 성능면에서 더 효율적일 수 있습니다. 비동기 프로그래밍은 주로 I/O 바운드 작업에서 그 장점을 발휘하므로, 작업의 성격을 정확히 이해하고 적절한 도구를 선택하는 것이 중요합니다.

### 파이썬의 라이프사이클 관리

- 프로그램 실행

  - 소스 코드 해석: 파이썬 프로그램이 시작되면, 파이썬 인터프리터는 먼저 소스 코드를 읽어 들입니다. 이 코드는 텍스트 파일(.py) 형태일 수도 있고, 이미 컴파일된 바이트코드(.pyc)일 수도 있습니다.
  - 컴파일: 소스 코드는 파이썬의 내장 컴파일러에 의해 바이트코드로 변환됩니다. 이 바이트코드는 파이썬 가상 머신(PVM)이 이해할 수 있는 중간 형태의 코드입니다.
  - 실행: 컴파일된 바이트코드는 파이썬 가상 머신에 의해 실행됩니다. PVM은 스택 기반의 인터프리터로서, 하나하나의 연산을 순차적으로 처리합니다.

- 메모리 관리 및 가비지 컬렉션

  - 자동 메모리 관리: 파이썬은 자동 메모리 관리를 제공합니다. 개발자는 객체 생성에만 집중하면, 생성된 객체의 메모리 할당은 파이썬 인터프리터가 자동으로 처리합니다.
  - 참조 카운팅: 파이썬은 객체의 참조 수를 추적하여 참조 카운트가 0이 되는 순간 객체를 메모리에서 해제합니다. 이는 가장 기본적인 메모리 관리 방식입니다.
  - 가비지 컬렉션: 참조 카운팅만으로는 해결할 수 없는 순환 참조 문제를 해결하기 위해 파이썬은 가비지 컬렉터를 포함하고 있습니다. 이는 주기적으로 메모리를 검사하여 도달할 수 없는 객체들을 찾아 메모리에서 해제합니다.
  - 세대별 수집(Generational Collection): 파이썬은 세대별 가비지 컬렉션 알고리즘을 사용합니다. 이는 객체를 생성된 지 얼마나 오래되었는지에 따라 여러 세대로 나누어 관리합니다. 젊은 세대의 객체에서 발생하는 가비지는 빈번하게 수집하고, 나이가 많은 세대는 덜 자주 수집합니다. 이 방법은 메모리 관리 효율을 최적화합니다.

- 종료 처리
  - 정리 작업: 프로그램이 종료될 때, 파이썬 인터프리터는 열려 있는 파일 핸들을 닫고, 네트워크 연결을 종료하고, 프로세스에 할당된 모든 시스템 리소스를 정리합니다.
  - 종료 코드 반환: 프로그램이 성공적으로 종료되었는지 또는 오류로 인해 종료되었는지를 나타내는 종료 코드를 운영 체제에 반환합니다.
