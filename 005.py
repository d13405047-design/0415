from collections import deque

# Stack simulation using list
stack = []
stack.append(10)  # push 10
stack.append(20)  # push 20
stack.pop()       # pop
stack.append(30)  # push 30
print('Final stack:', stack)

# Queue simulation using deque
queue = deque()
queue.append(10)  # enqueue 10
queue.append(20)  # enqueue 20
queue.popleft()   # dequeue
queue.append(30)  # enqueue 30
print('Final queue:', list(queue))
