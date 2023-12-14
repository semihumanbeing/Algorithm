
N = int(input())
works = [list(map(int, input().split())) for _ in range (N)]
dp = [0 for _ in range (N + 1)]

# 점화식
for idx in range(N + 1)[::-1]:
    # 남은 일 수가 넘어가면 인덱스 넘어가기
    if idx + works[idx][0] > N:
        dp[idx] = dp[idx + 1]
    else: 
        dp[idx] = max (dp[idx + works[idx][0]] + works[idx][1], dp[idx + 1])
