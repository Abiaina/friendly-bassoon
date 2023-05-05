# Python General Overview

## Compare Data Types

TODO table???
list vs linked list

## Methods

Where a is the variable.

- `type(a)` returns type of object
- Object Instantiation:

```
class Dog:
    def sing(self) :
        print("lalalala")

lola = Dog()
lola.sing()
```

# Special Libraries

- `from collections import X` Where X = counter, OrderedDict, ChainMap,
  - counter: Takes an array of items, creates dict with item as key and value as its frequency in array.
  - OrderedDict: a sub-class of dictionary but unlike dictionary, it remembers the order in which the keys were inserted.
  - ChainMap: encapsulates many dictionaries into a single unit and returns a list of dictionaries.
