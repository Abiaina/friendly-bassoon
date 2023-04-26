# Iterate through string.
ll = "This is a long string."
for l in ll:
    print(l)

i = 0
while i < len(ll):
    print(ll[i])
    i += 1

# Add to string.
# Concatenation.
print(ll + "extend the string")
ll = ll + "extend the string"

# Delete
# Removing the last added string.
ll = ll[:22]
print(ll)

# Reverse string.
# Reverse is a copy b/c strings are immutable.
print(ll[::-1])


# Reverse in place:
# Strings are immutable, therefore need to convert it to a list and assign it to itself.
i = 0
j = len(ll) - 1
print(ll)
ll = list(ll)
while i <= j:
    ll[i], ll[j] = ll[j], ll[i]
    i += 1
    j -= 1

# Note that ll is still a list object until converted back to string. The join returns a copy.
ll = "".join(ll)
print(ll)
# Undo reverse.
ll = ll[::-1]

# Replace

# Notice the switch from "" to ' in the replace command.
print(f"This is string with replace: {ll.replace('t', 'OOO')}")
print(f"Original list {ll}")

# Replace item in string with slice.
# Strings are not mutable, we are creating a new string.
# Replace item by index at ll[1].
ll_replace_by_index = ll[:1] + "***Star***" + ll[2:]
print(f"Replace by index with slice: {ll_replace_by_index}")

# Sort

# Use sorted to convert to sorted list.
# Join back into string.
sorted_list = sorted(ll)
sorted_string = "".join(sorted(ll))
print(f"Sorted list: {sorted_list}")
print(f"Sorted string: {sorted_string}")
print(f"Original sentence: {ll}")

# Convert to list (this is a copy) to use sort in place.
# Join back into string.
sentence_list = list(ll)
sentence_list.sort()
print(f"Sort list: {sentence_list}")
print(f"Sort string: {''.join(sentence_list)}")
print(f"Original sentence: {ll}")
