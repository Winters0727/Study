# def dfs(i, j): # recur
#     if maze[i][j] == '3':
#         return 1
#     else:
#         maze[i][j] = '1'
#         for k in range(4): # 상하좌우에
#             ni = i + di[k]
#             nj = j + dj[k]
#             if maze[ni][nj] != '1': # 벽이 아닌 칸이 있다면
#                 if dfs(ni, nj) == 1: # 이동, 목적지를 찾은 경우 중단
#                     return 1
#         return 0
#
# def dfs(i, j): # repeat
#     s = []
#     visited = [[0 for _ in range(16)] for _ in range(16)]
#     s.append((i, j))
#     visited[i][j] = 1
#     while s:
#         i, j = s.pop()
#         if maze[i][j] == '3': # 목적지에 다다르면 중단
#             return 1
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if maze[ni][nj] != '1' and visited[ni][nj] == 0: # 벽이 아니고 방문을 하지 않았다면
#                 s.append((ni, nj)) # 방문할 칸 목록에 push
#                 visited[ni][nj] = 1
#     return 0 # 목적지에 도착하지 못한 경우


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, 11):
    T = int(input())
    maze = [list(input()) for _ in range(16)]
    si, sj = -1, -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    answer = dfs(si, sj)
    print('#{0}'.format(tc),answer)