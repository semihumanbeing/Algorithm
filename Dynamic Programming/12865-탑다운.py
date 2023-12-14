#냅색
def recur(idx, weight):

    # 배낭의 무게가 물건의 무게랑 일치할 때
    if weight > B :
        return -999999

    #인덱스 끝까지
    if idx == A:
        return 0
    
    if dp[idx][weight] != -1 :
        return dp[idx][weight]

    # 물건을 넣은 경우
    dp[idx][weight] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx+1, weight))

    return dp[idx][weight]


A, B = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(A)]
dp = [[-1 for _ in range(100_001)] for _ in range(A)]

print(recur(0,0))
