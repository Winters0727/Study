def dfs1(n):
    visited[n] = 1
    print(n)
    for i in range(1, V+1):
        if adj[n][i] == 1 and visited[i] == 0: # 노드 i가 n에 인접이고 방문 전이면
            dfs1(i) # i노드로 이동

def dfs2(n, V): # 반복구조의 dfs
    s = [] # 스택 생성
    used = [0]*(V+1) # 중복확인
    s.append(n) # push(n) 시작점 저장
    used[n] = 1
    while len(s)!=0: # 스택이 비어있지 않으면
        n = s.pop() # pop(), 갈 수 있는 노드 중 하나를 꺼내 이동
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i]==1 and used[i]==0: # i가 인접이고, 스택에 들어있지 않으면
                s.append(i) # 인접 목록 추가
                used[i] = 1 # 목록에 추가 표시


# 일반 그래프

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접행렬
visited = [0 for _ in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 # 무방향 그래프

dfs2(1,V)

# 가중치 그래프

# V, E = map(int, input().split())
# edge = list(map(int, input().split()))
# adj = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접행렬
# visited = [0 for _ in range(V+1)]
# for i in range(E):
#     n1 = edge[i*3]
#     n2 = edge[i*3+1]
#     adj[n1][n2] = edge[i*3+2]