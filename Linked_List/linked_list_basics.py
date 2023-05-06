# Linked List


# Create Node
class NewNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create Linked List
class LinkedList:
    def __init__(self, node):
        self.head = node

    def add(self, node):
        current = self.head
        while current != None:
            current = current.next
        current.next = node


# Initialize Linked List.
n = NewNode("lola")
ll = LinkedList(n)

## Add to linked list.
current = ll.head
while current.next:
    current = current.next
add_data = ["selam", "loved", "laughter", "play"]
for i in add_data:
    current.next = NewNode(i)
    current = current.next

## Iterate through linked list.
# Loop
current = ll.head
while current:
    print(f"Iterative loop node data: {current.data}")
    current = current.next

print(f"Recursive loop node data")


# Recursive
def print_node(noodle):
    if not noodle:
        return
    else:
        print(noodle.data)
        print_node(noodle.next)


print_node(ll.head)

## Length
# Iterative.
current = ll.head
ll_count = 0
while current:
    ll_count += 1
    current = current.next
print(f"Number of nodes in linked list: {ll_count}")


# Recursive.
def length(noodle, count=0):
    if noodle:
        return length(noodle.next, count + 1)
    else:
        return count


# Why does this return None?
# Why do I need to return the recursive and the base case?
# The prints show the count iterating with every recursion.
# A) https://stackoverflow.com/questions/19215141/recursive-function-returning-none-in-python
# You need to return the recursive result
# otherwise the function simply ends after executing that statement,
# resulting in None being returned.
# You probably want to drop the else: and always return at the end:
# if not noodle:
#     print(f"Count:{count}")
#     return count
# else:
#     print(f"Count:{count}")
#     length(noodle.next, count + 1)


ll_count = length(ll.head)
print(f"Number of nodes in linked list: {ll_count}")

## Add to Link List.
# Front
new_node = NewNode("Add me to Front!")
new_node.next = ll.head
ll.head = new_node
print("See added node in front.")
print_node(ll.head)

# End
current = ll.head
while current.next:
    current = current.next
current.next = NewNode("Add me to End!")
print("See added node in end.")
print_node(ll.head)

# Not front or end
current = ll.head
while ll_count > 2:
    current = current.next
    ll_count -= 1

next = current.next
current.next = NewNode("Add me to somewhere")
current.next.next = next

## Delete from Linked List
print("Original Linked list.")
print_node(ll.head)
# Remove by order
# Remove 3rd node.
current = ll.head
last = None
count = 0
print("Removed 3rd Node.")
while count < 2:
    count += 1
    last = current
    current = current.next
print(f"Removed Node: {current.data}")
last.next = current.next
print_node(ll.head)

# Remove by value
last = None
current = ll.head
while current:
    if current.data == "Add me to somewhere":
        last.next = current.next
        break
    last = current
    current = current.next
print(f"Removed Node: {current.data}")
print_node(ll.head)

## Reverse Linked List.
# Reverse with copy
nodes = []
current = ll.head
while current:
    nodes.append(current.data)
    current = current.next
current = ll.head
nodes = nodes[::-1]
for n in nodes:
    current.data = n
    current = current.next

print("Reversed linked list, uses space.")
print_node(ll.head)

# Reverse in place.
last = None
next = None
current = ll.head
while current:
    next = current.next
    current.next = last
    last = current
    current = next
ll.head = last
print("Reverse in place.")
print_node(ll.head)

## Replace value.
current = ll.head
while current:
    if current.data == "Add me to End!":
        current.data = "This is the end."
        break
    current = current.next
print("Replaced Node Value.")
print_node(ll.head)

## Sort
# Create list of data + sort them.
# Put back in linked list.
# Remember when using sort, case matters.
# Upper case before lower case.
sort_list = []
current = ll.head
while current:
    sort_list.append(current.data.lower())
    current = current.next
sort_list.sort()
current = ll.head
for sl in sort_list:
    current.data = sl
    current = current.next

print("Print sorted linked list:")
print_node(ll.head)
