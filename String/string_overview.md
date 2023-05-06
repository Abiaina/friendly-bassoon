# Strings

- Strings are immutable in python, (you cannot change them inplace).
- Strings in Python are arrays of bytes representing unicode characters.
- Square brackets can be used to access elements of the string.
- Multi-line strings:

```
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
ut labore et dolore magna aliqua."""
```

## Methods

Where a is the string variable.
**Space**
_Time_

- `len(a)` : _0(1)_ ,
- `"free" in a`

#### Slice

- Slice:
  - `a[:5]` : slice from beginning to index 5 (not inclusive).
  - `a[2:5]` : slice from index 2 (inclusive) to index 5 (not inclusive).
  - `a[-5:-2]` : slice from reverse of list. Starts with -5 (inclsive) and stops at -2 (no inclusive).
    - `a = "World"`
    - `Wor`
- interpolation `f"Hello, {a}"` .
- `a.upper()`
- `a.lower()`

#### Reverse

- `"".join(reversed(a))` _O(n)_ **O(n)** returns a copy reversed string. Using slice `a[::-1]` does the same _O(n)_ **O(1)**.

- `a.strip()` removes whitespace from beginning/end
- `a.replace("X", "Y")` replace all instances of X with Y in a string. Pass empty string to remove characters by value. Returns a copy of the original string modified. **O(n)**, _O(n)_ .
- `a.split(",")` returns list of substrings segmented by the "," in original string.
- `a + b` can concatenate, returns combined string
- `a.format(age)` when a = `"I am {} old"`. Can insert unmodified number. Takes a set of values and you can call them by index in the {} of string.
- Escape value in string with `\`
- `a.find("test")` : Returns the first index of the first occurance of specific value, returns -1 if not found.
- `a.isdigit()` : returns True if all characters in string are digits, else False.

#### Join

- `",".join(myTuple)`: Join all items into string in tuple separated by ",". This joins any iterable into a string.
- `a.count("apple")`: counts the number of times apple appears in a string a.
- `a.encode()` : encodes the string (default is UTF-8).
- `a.endswith(".")` : Checks if string ends with a substring.

#### Sort

**Remember when using sort, case matters.** Uppercase before lowercase.

- `sorted(a)`: works on strings, but it returns a copy of the string as a sorted list.
- `a.sort()`: doesn't work on strings, convert string to a list (this is a copy) and then call sort on that list.

## TODO: Make table of common methods + Space/Time Complexity.

| Method                 | Time       | Space    | Description                                                                             |
| ---------------------- | ---------- | -------- | --------------------------------------------------------------------------------------- |
| `a.sort()`             | O(nlog(n)) | O(n)     | First make copy of string into list. Then call sort list in place and join into string. |
| `sorted(a)`            | O(nlog(n)) | O(n)     | Make copy of string into sorted list. Sort list in place.                               |
| `"".join(reversed(a))` | _O(n)_     | **O(n)** | returns a copy reversed string. Using slice `a[::-1]` does the same _O(n)_ **O(1)**.    |
| `a[::-1]`              | _O(n)_     | **O(1)** | Returns a copy reversed string with slice.                                              |
