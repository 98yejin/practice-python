class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self, data=None) -> None:
        self.head = Node(data)
        self._size = 0

    def __str__(self) -> str:
        current = self.head
        out = ""
        while current:
            out += str(current.data) + " -> "
            current = current.next
        return out[:-4]

    def isEmpty(self):
        return self._size == 0

    def size(self):
        return self._size

    def top(self):
        return self.head.data

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data


stack = Stack(3)
stack.push(1)
stack.push(2)
print(stack)
print(stack.pop())
print(stack)
