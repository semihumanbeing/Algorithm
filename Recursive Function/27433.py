import sys
sys.setrecursionlimit(100000)

N = int(input())

def recur(idx):
    if idx == 1:
        return 1
    
    return idx * recur(idx-1)

print(recur(N))