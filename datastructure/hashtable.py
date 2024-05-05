class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        if current and current.key == key:
            self.table[index] = current.next
            return
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
