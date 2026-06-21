from collections import deque

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        dx1, dy1, dx2, dy2 = x1 + dx[k], y1 + dy[k], x2 + dx[k], y2 + dy[k]

        if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
            next_pos.append({(dx1, dy1), (dx2, dy2)})

    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})

    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})

    print(next_pos)
    return next_pos # 현재 위치에서 이동할 수 있는 위치를 반환


def solution(board):

    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0

print(solution(board))