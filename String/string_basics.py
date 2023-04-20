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

### Note: Slice

- Slice:
  - `a[:5]` : slice from beginning to index 5 (not inclusive).
  - `a[2:5]` : slice from index 2 (inclusive) to index 5 (not inclusive).
  - `a[-5:-2]` : slice from reverse of list. Starts with -5 (inclsive) and stops at -2 (no inclusive).
    - `a = "World"`
    - `Wor`
- interpolation `f"Hello, {a}"` .
- `a.upper()`
- `a.lower()`

### Note: Reverse

- `"".join(reversed(a))` _O(n)_ **O(n)** returns a copy reversed string. Using slice `a[::-1]` does the same _O(n)_ **O(1)**.
- `a.strip()` removes whitespace from beginning/end
- `a.replace("X", "Y")` replace all instances of X with Y in a string. Pass empty string to remove characters by value. Returns a copy of the original string modified. **O(n)**, _O(n)_ .
- `a.split(",")` returns list of substrings segmented by the "," in original string.
- `a + b` can concatenate, returns combined string
- `a.format(age)` when a = `"I am {} old"`. Can insert unmodified number. Takes a set of values and you can call them by index in the {} of string.
- Escape value in string with `\`
- `a.find("test")` : Returns the first index of the first occurance of specific value, returns -1 if not found.
- `a.isdigit()` : returns True if all characters in string are digits, else False.

### Note: Join

- `",".join(myTuple)`: Join all items into string in tuple separated by ",". This joins any iterable into a string.
- `a.count("apple")`: counts the number of times apple appears in a string a.
- `a.encode()` : encodes the string (default is UTF-8).
- `a.endswith(".")` : Checks if string ends with a substring.

### Note: Sort
