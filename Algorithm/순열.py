def permutation(A,n,m,k): # A : 리스트, n : 0, m : 순열의 길이, k : 사용될 숫자의 개수
    if n == m: # 순열 완성
        print(''.join(list(map(str,p))))
    else:
        for i in range(k): # used를 왼쪽부터 숫자 k개 탐색
            if u[i] == 0: # 아직 사용되지 않은 숫자라면
                u[i] = 1
                p[n] = A[i]
                permutation(A, n+1, m, k) # 다음 자리를 결정하러 이동
                u[i] = 0 # 이전에 사용된 숫자를 원위치 해놓음

A = [1,2,3,4,5]
# p = [0] * m  # m개로 이루어진 순열을 만들 공간
u = [0] * len(A)  # 순열을 만들 때 사용될 리스트 A의 모든 숫자, 중복 사용 X
for case in range(1,len(A)+1):
    p = [0] * case
    permutation(A, 0, len(p), len(A))