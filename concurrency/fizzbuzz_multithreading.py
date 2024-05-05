import threading


def fizzbuzz(n):
    current = 1
    lock = threading.Lock()
    reached = threading.Condition(lock)

    def divisible_by_3():
        nonlocal current
        while current <= n:
            with lock:
                reached.wait_for(
                    lambda: current % 3 == 0 and current % 5 != 0 or current > n
                )
                if current > n:
                    break
                print("Fizz")
                current += 1
                reached.notify_all()

    def divisible_by_5():
        nonlocal current
        while current <= n:
            with lock:
                reached.wait_for(
                    lambda: current % 5 == 0 and current % 3 != 0 or current > n
                )
                if current > n:
                    break
                print("Buzz")
                current += 1
                reached.notify_all()

    def divisible_by_3_and_5():
        nonlocal current
        while current <= n:
            with lock:
                reached.wait_for(
                    lambda: current % 3 == 0 and current % 5 == 0 or current > n
                )
                if current > n:
                    break
                print("FizzBuzz")
                current += 1
                reached.notify_all()

    def not_divisible_by_3_or_5():
        nonlocal current
        while current <= n:
            with lock:
                reached.wait_for(
                    lambda: current % 3 != 0 and current % 5 != 0 or current > n
                )
                if current > n:
                    break
                print(current)
                current += 1
                reached.notify_all()

    threads = [
        threading.Thread(target=divisible_by_3),
        threading.Thread(target=divisible_by_5),
        threading.Thread(target=divisible_by_3_and_5),
        threading.Thread(target=not_divisible_by_3_or_5),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


from time import time

start = time()
fizzbuzz(10000)
print(start - time())
