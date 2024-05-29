# Practice Python 👩‍💻

## Contents

- Python Concurrency and Parallelism Problems : `good for understanding the concept of concurrency and parallelism`
  - Concurrent Web Scraper [link](/crawler/)
  - Parallel File Processing [link](/file_processing/)
  - Concurrent Producer-Consumer [link](/producer_consumer/)
- Concurrent Programming ( [Details](/concurrency/README.md) ) : `basic concepts of concurrent programming`
- Datastructures ( [Details](/datastructure/README.md) ) : `basic data structures and their implementations`
- Algorithms ( [Details](/algorithms/README.md) ): `basic algorithms and their implementations`
- FAQs : `frequently asked questions (not only Python)`

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

## Concurrent Programming ( [Details](/concurrency/README.md) )

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

## Datastructures ( [Details](/datastructure/README.md) )

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

## Algorithms ( [Details](/algorithms/README.md) )

| index | algorithm     | link                                |
| ----- | ------------- | ----------------------------------- |
| 1     | BFS           | [link](/algorithms/bfs.py)          |
| 2     | DFS           | [link](/algorithms/dfs.py)          |
| 3     | Binary Search | [link](/algorithms/binarysearch.py) |
| 4     | Quick Sort    | [link](/algorithms/quicksort.py)    |

## FAQs ( [Details](/faqs/README.md) )
