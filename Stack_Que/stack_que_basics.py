# Use this for que.
from collections import deque

# Stack are basically lists.
# LIFO
st = ["lola", "runs", "tired", 25]
print(f"Original stack: {st}")

# Push to Stack.
st.append("smiles")
print(f"Push to stack: {st}")

# Pop from Stack
popped = st.pop()
print(f"Popped from stack: {popped}")
print(f"Remaining stack: {st}")

# Pop from front of Stack
# O(n)
popped = st.pop(0)
print(f"Popped from front of stack: {popped}")
print(f"Remaining stack: {st}")

# See list for more methods to act on stack.

# Que
# Que are similar to lists.
# FIFO
# Use deque to make fast push/pop.
# Treat deque object like a list.
q = ["lola", "runs", "tired", 25]
dq = deque(q)
print(f"Original que type:{type(dq)} que: {dq}")

# Push to Que.
dq.append("smiles")
print(f"Push to que: {dq}")
print(f"Index of added item: {dq.index('smiles')} last idex: {len(dq) -1}")

# Pop from Que
# This works on both the list and deque object.
print(f"First item in  que: {dq[0]}")
popped = dq.pop()
print(f"Popped from que: {popped}")
print(f"Remaining que: {dq}")

# Pop from front of que
# O(1)
# To use pop(0) need to convert deque into list.
dq_list = list(dq)
popped = dq_list.pop(0)
print(f"Popped from front of que: {popped}")
print(f"Remaining que: {dq_list}")

# Use the left pop from front of que.
# Deque makes left pop take 0(1) time.
print(f"First item in  que: {dq[0]}")
popped = dq.popleft()
print(f"Popped from que: {popped}")
print(f"Remaining que: {dq}")

# See list for more methods to act on stack.
