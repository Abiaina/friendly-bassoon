# Arrays (Collections)

Organize data.

## Lists

- created via `[]` and `list(a)`
- they contain elements that are ordered(default add to end of list), **mutable** duplicate values of different data types.
- indexed from 0, or -1.

## Dictionary

- **ordered** and **mutable**. No duplicate keys.

## Tuple

- uses `()` to instantiate
- ordered (index starts at 0), **unmutable**, and allow duplicate values, any data types
- single item tuple requires comma: `("apple",)`

## Set

- Unordered, **mutable** and **unindexed**. No duplicate members. instantiate `{"apple"}`.
- Cannot not be iterated or changed by indexed.

## Methods

Where a is the array variable.
**Space**
_Time_

- `len(a)` : _0(1)_,
- `"free" in a`

### Dict

- `a.update({"key": "val"})` : Updates dict with specificied key-value pair. Adds new or replaces existing value.
- `a.keys()` : Returns list of keys.
- `a.values()`: Returns list of values
- `a.get(key)`: Gets value by key w/o error (`a[key]` raises error if no key).
- `dict.fromkeys()` : Returns dict with specfied keys and value (default None). Takes iterable for keys, single value for all values. Note `a` is not used.

### List

- `a.append(b)`: Adds element (b) to end of list a
- `a.clear()` : Removes all the elements from the **list & dict & set**.
- `a.copy()` : Returns copy of the **list & dict & set**
  - Shallow/deep copies: `a.copy()` returns a shallow copy of a. `a.deepcopy()` returns a deep copy of a.
  - When modifying the original **list & dict** after a copy, the changes will only show up in the shallow copy and original **list & dict**. Shallow copy still references original **list & dict** for nested elements. Deep copy won't reflect these changes.
- `a.count(b)` : Returns the count of b in a. **list & tuple**
- `a.index(b)` : Returns the index of element in a. **list & tuple**
- `a.pop()`: **list & dict & set (from [-1])** (_not tuples_)
  - **dict**: Removes element by key. `a.pop(key)`.
    - `a.popitem()` : Removes last inserted key-val pair. Returns them as tuple.
- `a.remove()` : Removes the first element with the specified value

##### Reverse

- `a.reverse()`: Reverses order of list in place.
- `a[::-1]`: Slices list and returns copy of reversed list.
- Symmetrical reassing iterating through list iteration.
  ```
  i = 0
  j = len(a) - 1
  while i <= j:
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
  ```

##### Slice

- Slice:
  - `a[:5]` : slice from beginning to index 5 (not inclusive).
  - `a[2:5]` : slice from index 2 (inclusive) to index 5 (not inclusive).
  - `a[-5:-2]` : slice from reverse of list. Starts with -5 (inclsive) and stops at -2 (no inclusive).
    - `a = ['W', 'o', 'r', 'l', 'd']`
    - `['W', 'o', 'r']`

##### Sort

**Remember when using sort, case matters.** Uppercase before lowercase. Cannot sort across types (all the elements need to be the same type).

- `sorted(a)`: returns a sorted list, copy.
- `a.sort()`: sort list in place. Timsort algorithm _O(n.logn)_ . Optional argument `reverse=True`.

##### Remove

- `a.remove('b')`: Remove first instance of b in list.
- `del a[0]`: remove element at index 0 of list.
- `a.pop`: Remove last element from list.

##### Add

- `a.insert(i, "b")` : Insert "b" at position `i` of list. If `i` is out of range of list, it goes to the closest position (ie index 10 of length 5 list, inserted at 5(end of list)).
- `a + [b]` : Combines lists, can only concatenate lists. Doesn't modify existing list, act on copy.
- `a.append(b)` : Adds to end of list, item can be any data object type.

##### Join

- `"".join(a)`: Join all items into string separated by "". This joins any iterable into a string, but items must be string type. Returns copy.

### Set

- `a.add(b)` : Can only add <b> once, set has no repeats.
- `a.pop()` : Removes element from set, returns removed element.
- `a.remove(b)` : Removes specific element from set.

### Tuple

**Tuple is unmutable**

- `a.count(b)` : Returns the count of b in a. **list & tuple**
- `a.index(b)` : Returns the index of element in a. **list & tuple**

## TODO: Make table of common methods + Space/Time Complexity.

| Method                 | Time       | Space    | Description                                                                             |
| ---------------------- | ---------- | -------- | --------------------------------------------------------------------------------------- |
| `a.sort()`             | O(nlog(n)) | O(n)     | First make copy of string into list. Then call sort list in place and join into string. |
| `sorted(a)`            | O(nlog(n)) | O(n)     | Make copy of string into sorted list. Sort list in place.                               |
| `"".join(reversed(a))` | _O(n)_     | **O(n)** | returns a copy reversed string. Using slice `a[::-1]` does the same _O(n)_ **O(1)**.    |
| `a[::-1]`              | _O(n)_     | **O(1)** | Returns a copy reversed string with slice.                                              |
