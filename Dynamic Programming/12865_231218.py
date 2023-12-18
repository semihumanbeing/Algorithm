import sys
input = sys.stdin.readline

def recur(idx, weight):

    if weight > K:
        return -99999
    
    if idx == N:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    dp[idx][weight] = max(recur(idx+1, weight+wv[idx][0])+wv[idx][1], recur(idx+1, weight))
    return dp[idx][weight]
    
N, K = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100_001)]for _ in range(N+1)]
    

print(recur(0,0))