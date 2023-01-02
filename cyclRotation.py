

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if A==[]:
        return A
    
    for x in range(K):
        element=A.pop()
        A.insert(0,element)
    return A 