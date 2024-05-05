import threading
from contextlib import contextmanager


class LockManager:
    def __init__(self):
        self.locks = {}
        self.lock_order = []
        self.thread_locks = threading.local()

    def declare_locks(self, *names):
        for name in names:
            if name not in self.locks:
                self.locks[name] = threading.Lock()
                self.lock_order.append(name)

    @contextmanager
    def acquire(self, *names):
        # 락 정렬: 이름 순서에 따라 정렬
        sorted_locks = sorted(names, key=lambda name: self.lock_order.index(name))

        # 스레드별로 현재 획득한 락 리스트를 가져오거나 새로운 리스트를 생성
        acquired = getattr(self.thread_locks, "acquired", [])

        # 락 획득 순서 위반 검사
        if acquired and any(
            self.lock_order.index(lock) >= self.lock_order.index(sorted_locks[0])
            for lock in acquired
        ):
            raise RuntimeError("Lock order violation")

        # 모든 락 획득 시도
        try:
            for name in sorted_locks:
                lock = self.locks[name]
                lock.acquire()
                acquired.append(name)
                self.thread_locks.acquired = (
                    acquired  # Update the thread's acquired locks list
                )
            yield
        finally:
            # 모든 락을 역순으로 해제
            for name in reversed(acquired):
                self.locks[name].release()
            # 획득한 락 리스트를 업데이트
            self.thread_locks.acquired = acquired[: -len(sorted_locks)]


# Example usage
lock_manager = LockManager()
lock_manager.declare_locks("lock1", "lock2", "lock3")


def thread_func():
    with lock_manager.acquire("lock1", "lock2"):
        print(f"{threading.current_thread().name} has acquired lock1 and lock2")
        import time

        time.sleep(1)


def thread_func2():
    with lock_manager.acquire("lock2", "lock3"):
        print(f"{threading.current_thread().name} has acquired lock2 and lock3")
        import time

        time.sleep(1)


thread1 = threading.Thread(target=thread_func)
thread2 = threading.Thread(target=thread_func2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
