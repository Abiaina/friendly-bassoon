# Stack & Queue

## Stack

- **LIFO**
- List with `a.append(b)` and `a.pop()` is a stack both O(1) time.

## Queue

- **FIFO**
- Use `a.append(b)` O(1) and and `a.pop()` O(N).
- Collections deque library is has `pop()

## Methods

Where a is the que or stack variable.
**Space**
_Time_

- `len(a)` : _0(1)_ ,

## Stack

- `a.pop()`: Pop from top of stack, returns popped item. _O(1)_
- `a.append(b)`: Push item (b) to top of stack. _O(1)_
- `a.pop(0)`: Pop from bottom of stack, returns popped item. _O(N)_
- Stack is a list, see list methods for other actions.

## Que

- `a.pop(0)` Pop from front of que, returns popped item. _O(N)_
- `a.append(b)`: Push item (b) to end of que. _O(1)_
- `a.pop()` Pop from end of que, returns popped item. Works for que list object and when que is a `deque` object. _O(1)_
- `a.popleft()` Pop from front of que, returns popped item. Works only on `deque` object _O(1)_
  - initialize deque object:
  ```
  from collections import deque
  a = deque(["lola", "complains", "play"])
  first = a.popleft()
  last = a.pop()
  a.append(last)
  a.append(first, 0)
  ```
  - You can still use `a.append(b)`, `a.pop()` and `a.popleft()` on the deque object.
- Que is a list, see list methods for other actions.

| Method        | Time | Space | Description                                              |
| ------------- | ---- | ----- | -------------------------------------------------------- |
| **Que**       |
| `a.pop()`     | O(n) | O(1)  | Returns removed item                                     |
| `a.append(b)` | O(1) | O(1)  |                                                          |
| `a.popleft()` | O(1) | O(1)  | Convert list to deque object, import from `collections`. |
| **Stack**     |
| `a.pop()`     | O(1) | O(1)  |                                                          |
| `a.append(b)` | O(1) | O(1)  |                                                          |
