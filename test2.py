import threading
from contextlib import contextmanager
from threading import Lock

# threading to stored information
_local = threading.local()


@contextmanager
def acquire(*locks):
    # Object identifier to sort the locks
    locks = sorted(locks, key=lambda x: id(x))

    # Checking the validity of previous locks
    acquired = getattr(_local, "acquired", [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("Lock Order Violation")

    # Collecting all the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        # Acquiring all the locks
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Locks are released in reverse order
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks) :]  # removing the locks from the list


# Define locks
lock1 = Lock()
lock2 = Lock()


# Define thread functions
def thread_func1():
    with acquire(lock1, lock2):
        print(f"{threading.current_thread().name} has acquired both locks")
        # Simulate some operations
        import time

        time.sleep(1)


def thread_func2():
    with acquire(lock2, lock1):
        print(f"{threading.current_thread().name} has acquired both locks")
        # Simulate some operations
        import time

        time.sleep(1)


# Create threads
t1 = threading.Thread(target=thread_func1, name="Thread-1")
t2 = threading.Thread(target=thread_func2, name="Thread-2")

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
