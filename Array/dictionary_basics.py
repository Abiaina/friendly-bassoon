# This doesn't have to be installed via pip.
import copy

# Create dict.
ll_empty_dict = {}
ll_nest_list = [["t", 2], ["f", 4]]
ll_dict = dict(ll_nest_list)
print(f"Empty initialized dict: {ll_empty_dict} type: {type(ll_empty_dict)}")
print(f"Nested list: {ll_nest_list}")
print(f"Initialized dict from nest list and dict(): {ll_dict}")

# Iterate through dict.
ll = {
    "a": 24,
    "b": "catdog",
    "aa": "catdog",
    "e": "large element",
    "nest": ["nested", "element"],
    "bery nest": {"first": 1, "thyme": 2},
}

# Iterate through keys in dict.
# Cannot iterate through keys via index, unless you use the .keys() method.
# The index refs the index key:val in dict.
for l in ll:
    print(l)

# Get keys:
keys = ll.keys()
print(f"These are keys: {keys}")
# Get Values:
values = ll.values()
print(f"These are values: {values}")

# Iterate through key values.
# Can use index or .items().
for key, val in ll.items():
    print(f"{key} : {val}")

# Copy a dict..
copy_ll = ll.copy()
deep_copy_ll = copy.deepcopy(ll)
# Modifying the original dict.
# This will only show up in the shallow copy and original dict.
# Shallow copy still references original dict for nested elements.
# Also, see nested element replaced (dicts are mutable).
ll["nest"][-1] = "surprise"
print(f"original id: {id(ll)}, original dict: {ll}")
print(f"copy id: {id(copy_ll)}, copy dict: {copy_ll}")
print(f"deep copy id: {id(deep_copy_ll)}, deep copy dict: {deep_copy_ll}")

# Get Value by key without error on fail.
ll.get("nest")
ll.get("not a key")

# Update Dict.
ll.update({"new key": "surprise"})
ll.update({"nest": ["updated", "nested", "value"]})

# # Reverse dict.
# This is a copy b/c we get item-dict of items
# Convert the item-dict into list.
# Reverse the list, create dict from nested list.
list_of_items = list(ll.items())
# This step is separated b/c reverse in place returns none.
list_of_items.reverse()
ll_reversed_dict = dict(list_of_items)
print(f"Reversed dict: {ll_reversed_dict}")
print(f"Original unmodified dict: {ll}")


# Add new item, can also use update.
ll["now"] = "current time"
print(f"Added new item to dict: {ll}")


# Delete & Remove
del ll["now"]
print(f"Dict should not contain 'now' key. {ll.get('now')}")

# Sort
# Dict is sorted by default.

# Get Items by last insert.
# Get and removes last inserted item.
# Returns the item as a tuple (indexable)
last_insert = ll.popitem()
print(last_insert)


# # Replace
# Use the dict[key] = val to replace the key:value pair.
# --OR-- Use update().
# Iterate through dict and update by value:
# use update() --OR-- dict[key] = value.

# Create dict from specific keys + single default value.
simple_dict = dict.fromkeys(['new key', 'aa'], 1)
print(simple_dict)
