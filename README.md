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

#### Tree

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

#### Tries

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

#### Graph

- 트리는 사이클이 없는 하나의 연결 그래프임.
- 그래프가 트리보다 큰 개념임.
- 그래프는 단순히 노드와 그 노드를 연결하는 간선(edge)을 하나로 모아놓은 것임
- 방향성이 있을 수도 있고 없을 수도 있음.
- 사이클이 존재하지 않을 수도 있고 acycle graph 라고 부름
- 그래프는 여러개의 고립된 부분 그래프(isolated subgraphs)로 구성될 수 있고, 모든 정점 쌍(pair of vertices) 간에 경로가 존재하는 그래프는 연결 그래프라고 부름.

[그래프 탐색]

- Depth-first search ( 모든 노드를 방문하고자 할 때 선호됨, 반드시 어떤 노드를 방문했는지 체크해야함. 안그러면 무한루프 빠지기 쉬움 )
- Breadth-first search ( 최단 경로 또는 임의의 경로, Queue 사용 )

#### Stack

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

#### Queue

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

#### Heapq ( priority queue )

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

#### List

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

#### Hash Table

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
