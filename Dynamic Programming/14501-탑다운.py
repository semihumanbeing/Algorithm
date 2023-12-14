
def recur(idx):

    if idx == N -1 :
        return 0
    if idx > N - 1:
        return -99999
    
    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recur(idx + works[idx][0]) + works[idx][1], recur(idx + 1))

    return dp[idx]
    

N = int(input())
works = [list(map(int, input().split())) for _ in range (N)]
dp = [-1 for _ in range (N + 1)]

print(recur(0))