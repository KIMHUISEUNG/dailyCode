# -*- coding: utf-8 -*-
# 미로탈출.py

'''
BFS 활용 문제
input :
5 6
101010
111111
000001
111111
111111

output : 10
'''

from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def maze_escape(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 확인한 후 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 괴물이 있는 곳 이동 X
            if graph[nx][ny] == 0:
                continue

            # 괴물이 없는 곳 이동 O
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 해당 좌표의 값 1증가
                queue.append((nx, ny))

        #print(queue)
    # 최단 거리 이동 거리 반환, 이동할 때마다 +1 증가한 최종 값
    return graph[n-1][m-1]


print(maze_escape(0, 0))