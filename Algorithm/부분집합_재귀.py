def powset_recur(n, k):
    if n == k:
        for i in range(k):
            if L[i] == 1:
                print(A[i], end = '')
        print(L)
    else:
        L[n] = 0
        powset_recur(n+1, k)
        L[n] = 1
        powset_recur(n+1, k)

A = [1,2,3]
L = [0]*len(A)
powset_recur(0,len(A))