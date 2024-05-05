import threading

# Create a semaphore with an initial value of 1
semaphore = threading.Semaphore(1)


def semaphored_function():
    semaphore.acquire()
    try:
        # Code that needs to be synchronized
        print("This is a semaphored function.")
    finally:
        semaphore.release()


# Create threads that use the semaphored function
thread1 = threading.Thread(target=semaphored_function)
thread2 = threading.Thread(target=semaphored_function)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
