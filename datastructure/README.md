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
