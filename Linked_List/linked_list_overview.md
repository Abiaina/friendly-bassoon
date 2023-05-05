# Linked List

Create with Node object (data + next) + Linked List (head) object.

There are also doubly linked lists, each Node has data, next and previous.

### Algorithims

https://www.techinterviewhandbook.org/algorithms/linked-list/

- 2 pointers: Fast & Slow pointers help find:
  - midpoint
  - presence of loops

### Actions

- Traverse linked list: O(N)
- Search: O(N)
- Insert Node

  - O(1) for head add
  - O(N) for add (traverse list to find position)

- Remove Node
  - O(1) for head removal
  - O(N) for add (traverse list to find position)
- Reverse linked list in place
- Merge 2 linked list
- Find Midpoint
- Count number of nodes
- Reorder List: https://leetcode.com/problems/reorder-list/

| Method        | Time | Space | Description                                              |
| ------------- | ---- | ----- | -------------------------------------------------------- |
| **Que**       |
| `a.pop()`     | O(n) | O(1)  | Returns removed item                                     |
| `a.append(b)` | O(1) | O(1)  |                                                          |
| `a.popleft()` | O(1) | O(1)  | Convert list to deque object, import from `collections`. |
| **Stack**     |
| `a.pop()`     | O(1) | O(1)  |                                                          |
| `a.append(b)` | O(1) | O(1)  |                                                          |
