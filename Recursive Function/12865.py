def recur(idx, weight, value):
    global answer 

    if (weight > B):
        return
    if (idx == A):
        answer = max(answer, value)
        return
    
    # 물건을 넣은 경우
    recur(idx + 1, weight + items[idx][0], value + items[idx][1])

    # 물건을 넣지 않은 경우
    recur(idx, weight, value)



A, B = map(int, input().split())
items = [list(map(int, input().split()))for _ in range(A)]
answer = 0

recur(0, 0, 0)
print(answer)