def bag():

    for idx in range(A + 1):
        for weight in range(B + 1):
            if weight < B :
                dp[idx][weight] = dp[idx-1][weight]
            else: 
                dp[idx][weight] = max(dp[idx - 1][weight - items[idx][0]] + items[idx][1], dp[idx - 1][weight])
    


#냅색
A, B = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(A)]
dp = [[0 for _ in range(B + 1)] for _ in range(A + 1)]
