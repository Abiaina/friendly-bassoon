# This doesn't have to be installed via pip.
import copy

# Tuple.
tt = ("a", "b", "a", "aa", "e", "large element")
# Set
s = {"a", "b", "aa", "e", "large element"}

print(f"This is a set: {s}")
# Iterate through set.
# Cannot use index to iterate through set.
# Set is unordered and unindexed
for se in s:
    print(se)

# Iterate through set.
# Can index and iterate through a tuple.
print(f"This is a tuple: {tt}")
i = 0
while i < len(tt):
    print(tt[i])
    i += 1

# Count items in tuple.
# Set doesn't allow duplicates,
# Count will always be 0 or 1 for set.
# Tuples allow duplicates and are ordered.
print(f"count of item in list: {tt.count(tt[0])}")

item_count = 0
item = tt[0]
for i in tt:
    if i == item:
        item_count += 1
print(f"count of item in tuple: {item_count}")

# Add & Insert.
# Tuple are unmutable.
# Set are mutable.
print(f"Original set: {s}")
s.add("apple")

# Delete & Remove
s.pop()
s.remove("apple")

# Creates copy of set.
s_copry = s.copy()
deep_copy_list = copy.deepcopy(s)
