from collections import deque

def DFS(edge_list, S):
    global V, stack
    result = [S]
    stack.append(S)
    visited = [0 for _ in range(V+1)]
    visited[S] = 1
    while stack:
        for j in range(1, V+1):
            if edge_list[stack[-1]][j] == 1 and visited[j] == 0:
                visited[j] = 1
                stack.append(j)
                result.append(j)
                break
        else:
            stack.pop()
    return result

def BFS(edge_list, S):
    global V, queue
    result = [S]
    queue.append(S)
    visited = [0 for _ in range(V+1)]
    visited[S] = 1
    while queue:
        for j in range(1, V+1):
            if edge_list[queue[0]][j] == 1 and visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                result.append(j)
                break
        else:
            queue.popleft()
    return result

V = int(input())
edge_list = []
stack, queue = deque(), deque()