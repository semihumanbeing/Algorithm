import math, functools
def gcdArray(a, b):
    if b == 0:
        return a 
    return gcdArray(b, a%b)


def solution(arr):
    t = 1
    p = 1
    for i in range(1, len(arr)):
        t *= arr[i-1]
        p *= gcdArray(arr[i], arr[i-1])
    
    return p

arr = [1,2,3]
print(solution(arr))