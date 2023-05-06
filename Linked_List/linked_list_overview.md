# Linked List

Create with Node object (data + next) + Linked List (head) object.

There are also doubly linked lists, each Node has data, next and previous.

### Algorithims

##### 2 pointers: Fast & Slow pointers help find

- **get kth from last node**: Have two pointers, where one is k nodes ahead of the other. When the node ahead reaches the end, the other node is k nodes behind
- **midpoint**: Have two pointers, where one pointer increments twice as much as the other. When the faster node reaches the end of the list, the slower node will be at the middle
- **loops**:
  - _Has loop_: Have two pointers, where one pointer increments twice as much as the other, if the two pointers meet, means that there is a cycle.
  - _Start of loop_:
    1. If a loop is found, initialize a slow pointer to head, let fast pointer be at its position.
    1. Move both slow and fast pointers one node at a time.
    1. The point at which they meet is the start of the loop.

### Actions

_Time_ **Space**

##### Traverse linked list: Iterative or Recursive (see example)

##### Search

- _O(N)_

##### Insert Node

- _O(1)_ for head add
- _O(N)_ for add (traverse list to find position)

##### Remove Node

- _O(1)_ for head removal
- _O(N)_ for add (traverse list to find position)

##### Reverse linked list in place

1. Has `Current=Head`, `Last=None` and `Next=None`
1. Iterate through linked list:
   - Next = Current.next
   - Current.next = Last
   - Last = Current
   - Current = Next

##### Merge 2 linked list

TODO: Add how to

##### Reorder List

TODO: https://leetcode.com/problems/reorder-list/

| Method        | Time | Space | Description                                              |
| ------------- | ---- | ----- | -------------------------------------------------------- |
| **Que**       |
| `a.pop()`     | O(n) | O(1)  | Returns removed item                                     |
| `a.append(b)` | O(1) | O(1)  |                                                          |
| `a.popleft()` | O(1) | O(1)  | Convert list to deque object, import from `collections`. |
| **Stack**     |
| `a.pop()`     | O(1) | O(1)  |                                                          |
| `a.append(b)` | O(1) | O(1)  |                                                          |
