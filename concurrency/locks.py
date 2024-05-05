import threading
from time import sleep

# Create a lock
lock = threading.Lock()


def locked_function(i):
    with lock:
        # Code that needs to be synchronized
        print(f"This is a locked function in thread {i}")
    sleep(1)
    print(f"end sleep {i}")


# Create threads that use the locked function
thread1 = threading.Thread(target=locked_function, args=[1])
thread2 = threading.Thread(target=locked_function, args=[2])

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
