'''

큐: 선입선출(FIFO)

'''


from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.append(4)
queue.append(2)
queue.popleft()
print(queue)