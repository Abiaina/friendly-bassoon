# Iterate through string.
ll = "This is a long string."
for l in ll:
    print(l)

i = 0
while i < len(ll):
    print(ll[i])
    i += 1


# Reverse string.

# Reverse a copy.
print(ll[::-1])

# Reverse in place:
# Strings are immutable, therefore need to convert it to a list.
i = 0
j = len(ll) -1
print(ll)
ll = list(ll)
while i <= j:
    ll[i], ll[j] = ll[j], ll[i]
    i += 1
    j -= 1
# Note that ll is still a list object until converted back to string. The join returns a copy.
ll = "".join(ll)
print(ll)

# Replace
print(ll.replace("t", "OOO"))
print(f"This is string post replace: {ll}")

# Sort
# Convert to list or use sorted to convert to sorted list.
# Join back into string.
sorted_list = ll.split(" ").sort()
print(f"Sorted list: {sorted_list}")
print(f"Original list {ll}")