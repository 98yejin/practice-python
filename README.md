# Practice Python 👩‍💻

## Python Concurrency and Parallelism

### [Concurrent Web Scraper](/crawler/)

- Objective: Implement a concurrent web scraper that retrieves data from multiple web pages simultaneously.
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
  - Apply a specific operation to each file (e.g., compression, encryption, or analysis).
  - Display the progress and status of the file processing.
- Extension: Implement error handling and logging for file processing failures.

### [Concurrent Producer-Consumer](/producer_consumer/)

- Objective: Implement a concurrent producer-consumer system using threads.
- Requirements:
  - Create a shared queue to store data items.
  - Implement producer threads that generate and add data items to the queue.
  - Implement consumer threads that retrieve and process data items from the queue.
  - Use synchronization primitives (e.g., locks or semaphores) to ensure thread safety.
  - Display the production and consumption of data items.
- Extension: Implement a mechanism to gracefully terminate the producer and consumer threads.
