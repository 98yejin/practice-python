class BinaryHeap(object):
    """
    BinaryHeap class represents a binary heap data structure.
    """

    def __init__(self) -> None:
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        """
        Helper method to percolate up the last inserted element in the heap.
        """

        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        """
        Inserts an element into the binary heap.
        Args:
            k: The element to be inserted.
        """

        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        """
        Helper method to percolate down the element at the given index in the heap.
        Args:
            idx: The index of the element to be percolated down.
        """

        left = idx * 2
        right = idx * 2 + 1
        smallest = idx
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        if smallest != idx:
            self.items[idx], self.items[smallest] = (
                self.items[smallest],
                self.items[idx],
            )

    def extract(self):
        """
        Removes and returns the minimum element from the binary heap.
        Returns:
            The minimum element from the binary heap.
        """

        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
