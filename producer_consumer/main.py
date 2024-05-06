import random
import time
import queue
import threading

buffer = queue.Queue(maxsize=10)


def producer(data_queue: queue.Queue):
    """
    Producer function that generates random items and puts them into the data queue.

    Args:
        data_queue (queue.Queue): The queue to put the generated items into.

    Returns:
        None
    """
    while True:
        item = random.randint(1, 100)
        data_queue.put(item)
        print(f"Producer: Produced {item}")
        time.sleep(random.randint(1, 5))
        if random.random() <= 0.1:
            print(f"Producer put None...")
            data_queue.put(None)
            break


def consumer(data_queue: queue.Queue):
    """
    Consumer function that consumes items from the data queue.

    Args:
        data_queue (queue.Queue): The queue from which items are consumed.

    Returns:
        None
    """
    while True:
        item = data_queue.get()
        if item is None:
            break
        print(f"Consumer: Consumed {item}")
        time.sleep(random.randint(1, 5))
    print(f"Consumer terminated...")


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer, args=(buffer,), daemon=True)
    consumer_thread = threading.Thread(target=consumer, args=(buffer,), daemon=True)
    producer_thread.start()
    consumer_thread.start()
    try:
        producer_thread.join()
        consumer_thread.join()
    except KeyboardInterrupt:
        print("Terminated by user")
    print("Done!")
