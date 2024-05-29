## Algorithms

| index | algorithm     | link                                |
| ----- | ------------- | ----------------------------------- |
| 1     | BFS           | [link](/algorithms/bfs.py)          |
| 2     | DFS           | [link](/algorithms/dfs.py)          |
| 3     | Binary Search | [link](/algorithms/binarysearch.py) |
| 4     | Quick Sort    | [link](/algorithms/quicksort.py)    |

### Breadth-First Search (BFS)

[Time Complexity]

O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

[Space Complexity]

O(V), where V is the number of vertices. In the worst case, the entire graph may need to be stored in the queue.

[When to use]

BFS is used to explore the vertices of a graph level by level, starting from a given source vertex. It is often used to find the shortest path in unweighted graphs, connected components, and more.

### Depth-First Search (DFS)

[Time Complexity]

O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. However, DFS can be faster in practice for some graph structures.

[Space Complexity]

O(V), where V is the number of vertices. In the worst case, the entire graph may need to be stored in the call stack.

[When to use]

DFS is used to explore the vertices of a graph deeply, following each branch until it reaches a dead end before backtracking. It is often used for topological sorting, cycle detection, maze solving, and more.

### Binary Search

[Time Complexity]

- O(log n), where n is the number of elements in the sorted array.
- if the array is not sorted, binary search cannot reliably find the target element. In such cases, alternative methods such as linear search (iterating through the array sequentially) may be used to find the target element, but with a time complexity of O(n) instead of O(log n) provided by binary search on a sorted array.

[Space Complexity]

O(1). Binary search is an in-place algorithm and does not require additional space.

[When to use]

Binary search is used to find the position of a target value within a sorted array efficiently. It repeatedly divides the search interval in half until the target value is found or the interval becomes empty.

### Merge Sort

[Time Complexity]

O(n log n), where n is the number of elements in the array.

[Space Complexity]

O(n), where n is the number of elements in the array. Merge sort requires additional space for merging subarrays during the merge step.

[How it works]

- Merge sort is a divide-and-conquer algorithm that recursively divides the array into smaller subarrays, sorts them independently, and then merges the sorted subarrays to produce the final sorted array.
- It is a stable sorting algorithm and is often used for sorting large datasets efficiently.

[Why to use]

- Efficiency: Merge sort has a time complexity of O(n log n) in all cases, making it efficient for sorting large datasets. Therefore, it is suitable for applications where sorting performance is important.
- Stability: Merge sort is a stable sorting algorithm, meaning it maintains the relative order of equal elements. This property is important in scenarios where the original order of equal elements needs to be preserved.
- Divide and conquer: Merge sort follows a divide and conquer strategy by recursively dividing the sorting problem into smaller subproblems, independently sorting them, and then merging the sorted subarrays. This makes it easier to implement and understand compared to other sorting algorithms.
- Predictable performance: Merge sort exhibits consistent performance characteristics and does not suffer from worst-case scenarios like some other sorting algorithms. It performs well on datasets of varying sizes and distributions.
- Not In-Place: Merge sort is not an in-place sorting algorithm and requires additional memory for merging subarrays. However, the efficiency and stability advantages often outweigh this overhead.

### Quick Sort

[Time Complexity]

O(n log n) on average, O(n^2) in the worst case, where n is the number of elements in the array.

[Space Complexity]

O(log n) on average, O(n) in the worst case due to recursive calls. Quick sort is an in-place sorting algorithm and does not require additional space for sorting.

[How it works]

- Quick sort is a divide-and-conquer algorithm that recursively partitions the array into smaller subarrays based on a pivot element, sorts the subarrays independently, and then combines them to produce the final sorted array.
- It is widely used in practice due to its efficiency on average and ease of implementation.
