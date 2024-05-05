import threading

# Create a barrier for 2 threads
barrier = threading.Barrier(2)


def barriered_function():
    print("Before barrier")
    print("mess??")
    barrier.wait()
    # Code that needs to be synchronized
    print("This is a barriered function.")
    print("in order...")
    print("right?")


# Create threads that use the barriered function
thread1 = threading.Thread(target=barriered_function)
thread2 = threading.Thread(target=barriered_function)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
