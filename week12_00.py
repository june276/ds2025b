from collections import deque

d = deque([3, -9, 24])
d.append(77)
d.append(91)

for i in range(len(d)):
    print(d.popleft())