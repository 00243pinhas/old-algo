def solution(N):

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    binary_N=bin(N)
   

    min_gap=0
    max_gam=0

    for x in binary_N[3:]:

        if x=='0':
            min_gap+=1
        
        if x=='1':
            
            if max_gam < min_gap:
                max_gam=min_gap
            
            min_gap=0
    
    return max_gam
    