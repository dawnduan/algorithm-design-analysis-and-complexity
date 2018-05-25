#code
def recursion_step(n, lis, q):
    if n == 0:
        return 1
    if q[n] > 0:
        print('haha')
        return q[n]
    cnt = n-1
    while cnt >= 0:
        if lis[cnt] < lis[n]:
            return 1 + recursion_step(cnt, lis, q)
            
        if cnt == 0:
            return 1
            
        cnt -= 1
    # cnt == 0 && lis[0] > lis[n]
    
lis = [0,52,-3, -2,4,6]; n = len(lis)
q = [0 for i in range(n)]
print(recursion_step(5, lis, q))

    
def find_my_len(n, lis):
    '''
    starting from the head of the list
    for each element perform the recursion step so that 
    '''
    for i in range(n):
        q[i] = recursion_step(i, lis, q)

def get_my_lis(q, lis):
    l = []
    k = lis.index(max(q))
    while q[k] >= 0:
        l.append(lis[k])
        cnt = k-1
        if q[k] == 1: #end 
            return l
        while q >= 0:
            # next candidate
            if (lis[cnt] < lis[k]) & (q[cnt] == q[k]-1):
                k = cnt
                break
            cnt -= 1
    return l
