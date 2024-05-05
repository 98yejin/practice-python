import threading

# Shared resource: a global variable
counter = 0
lock = threading.Lock()


# Function that increments the counter
def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1


# Create two threads that increment the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

# Expected value of counter: 2000000
print("Final value of counter:", counter)
