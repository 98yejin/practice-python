class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertToHead(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertToTail(self, data):
        node = Node(data)
        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
            prev = current
            current = current.next

    def print(self):
        current = self.head
        while current:
            print(f"{current.data} -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"{data} exists!")
                return True
            current = current.next
        print(f"{data} not exists!")
        return False


ll = LinkedList()
ll.insertToHead(1)
ll.print()
ll.insertToHead(2)
ll.print()
ll.insertToHead(3)
ll.print()
ll.insertToTail(4)
ll.print()
ll.insertToTail(5)
ll.print()
ll.search(5)
ll.search(111)
ll.delete(1)
ll.delete(3)
ll.delete(5)
ll.print()
