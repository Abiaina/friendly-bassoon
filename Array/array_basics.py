# This doesn't have to be installed via pip.
import copy

# Iterate through list.
ll = ["a", "b", "a", "aa", "e", "large element", ["nested", "element"]]
for l in ll:
    print(l)

i = 0
while i < len(ll):
    print(ll[i])
    i += 1

# Copy a list.
copy_ll = ll.copy()
deep_copy_ll = copy.deepcopy(ll)
# Modifying the original list.
# This will only show up in the shallow copy and original list.
# Shallow copy still references original list for nested elements.
# Also, see nested element replaced (lists are mutable).
ll[-1][-1] = "surprise"
print(f"original id: {id(ll)}, original list: {ll}")
print(f"copy id: {id(copy_ll)}, copy list: {copy_ll}")
print(f"deep copy id: {id(deep_copy_ll)}, deep copy list: {deep_copy_ll}")

# Count items in list.
print(f"count of item in list: {ll.count(ll[0])}")

item_count = 0
item = ll[0]
for i in ll:
    if i == item:
        item_count += 1
print(f"count of item in list: {item_count}")

# Reverse list.
# This is a copy b/c it's slice of original list.
print(f"Reverse with slice: {ll[::-1]}")
print(f"Original unmodified list: {ll}")

# Reverse in place
ll.reverse()
print(f"Reverse in-place: {ll}")
print(f"Original list is now reversed: {ll}")

# Reverse in place:
i = 0
j = len(ll) - 1
while i <= j:
    ll[i], ll[j] = ll[j], ll[i]
    i += 1
    j -= 1
print(f"Original list is now reversed back via manual reverse in place: {ll}")

# Add & Insert.
ll = ll + ["now"]
print(f"Concatenated list: {ll}")
ll.insert(0, "hip-hop")
print(f"Inserted list: {ll}")
ll.append("me")
print(f"Appended list: {ll}")

# Delete & Remove
ll.pop()
print(f"Popped list: {ll}")
ll.remove("hip-hop")
print(f"Removed list: {ll}")
del ll[-1]
print(f"Deleted list: {ll}")


# Sort

# Cannot sort between list and str.
# Cannot sort mixed nested lists.
# Removing the nested list.
ll.pop()

# Creates copy of list that is sorted.
sorted_list = sorted(ll)
print(f"Sorted list: {sorted_list}")
print(f"Original list: {ll}")

# Sorts list in place.
# Using deep copy b/c I don't want to modify the original list.
# Acts list object directly.
deep_copy_list = copy.deepcopy(ll)
deep_copy_list.sort()
print(f"Sorted list: {deep_copy_list}")
deep_copy_list.sort(reverse=True)
print(f"Reverse sorted list: {deep_copy_list}")
print(f"Original list: {ll}")


# # Note that ll is still a list object until converted back to string. The join returns a copy.
# ll = "".join(ll)
# print(ll)
# # Undo reverse.
# ll = ll[::-1]

# # Replace
# # Notice the switch from "" to ' in the replace command.
# print(f"This is string with replace: {ll.replace('t', 'OOO')}")
# print(f"Original list {ll}")
