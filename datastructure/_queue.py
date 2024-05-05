class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
        self._size = 0

    def __str__(self) -> str:
        current = self.front
        out = ""
        while current:
            out += f"{current.data} => "
            current = current.next
        return out

    def enqueue(self, item):
        if self.isEmpty():
            self.front = self.rear = Node(item)
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty. Failed to Dequeue!")
        data = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self._size -= 1
        return data

    def isEmpty(self):
        return self._size == 0
