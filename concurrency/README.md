## Concurrency

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

1. [Concurrent Web Scraper](/crawler/)
2. [Parallel File Processing](/file_processing/)
3. [Concurrent Producer-Consumer](/producer_consumer/)

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
