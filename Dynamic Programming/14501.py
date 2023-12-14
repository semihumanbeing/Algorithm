
def recur(idx):
    global answer

    # 인덱스가 N의 하루 전 날이면 0을 리턴한다
    if idx == N-1:
        return 0
    # 인덱스가 N의 하루 전 날 보다 커지면 -99999 를 리턴한다
    if idx > N-1:
        return -9999999
    # 만약 인덱스값이 이미 들어가있으면 그 값을 사용한다
    if dp[idx] != -1:
        return dp[idx]
    
    # 2개의 재귀함수 결과 중 가장 큰값을 dp 인덱스에 넣는다
    dp[idx] = max( recur(idx + work[idx][0]) + work[idx][1], recur(idx + 1))
    
    return dp[idx]


N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(N + 1)]
answer = 0

recur(0)
print(max(dp))