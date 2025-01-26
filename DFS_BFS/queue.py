from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue.popleft()) # deque
queue.append(1)
queue.append(4)
queue.append(4)
print(queue.popleft())

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 변경
queue = list(queue)
print(queue) # 나중에 들어온 원소부터 출력
