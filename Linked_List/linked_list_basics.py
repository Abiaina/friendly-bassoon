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


# Recursive
def print_node(noodle):
    if not noodle:
        return
    else:
        print(f"Recursive loop node data: {noodle.data}")
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

## Delete from Linked List

# Remove by order

# Remove by value

## Reverse Linked List.
# Reverse with copy

# Reverse in place.

## Replace value.

## Sort
