def solution(A):
    # write your code in Python 3.8.10
    pass

    # duplicate=[]

    for x in range(0,len(A),1):
        for y in range(0,len(A),1):
            if x!=y:
                if A[x]==A[y]:
                    # duplicate.append(A[x])
                    A[x]='x'
                    A[y]='x'
    
    for x in A:
        if x!='x':
            return x


# not really efficase With 