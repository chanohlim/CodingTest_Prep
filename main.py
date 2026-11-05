from collections import deque

N = 1000
K = 500

q = deque([i for i in range(1, N+1)])
print(q)

while len(q) > 1:
    for i in range((K - 1) % len(q)):
        q.append(q.popleft())

    q.popleft()

    print(q)

print(q[0])