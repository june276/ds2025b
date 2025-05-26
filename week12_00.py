from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(g, i, visited):
    queue = deque([i]) #popleft(), append() 성능 때문에 큐처럼 쓰기위해 사용
    visited[i] = True
    while queue:
        # print(visited)
        i=queue.popleft() # dequeue
        print(chr(ord('A') + i), end= ' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True


visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]
dfs(graph, 7, visited_dfs)
print()
bfs(graph, 6, visited_bfs)