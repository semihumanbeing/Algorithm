
def recur(idx, price):

    if idx == N-1:
        answer = max(answer, price)
        return 
    if idx > N-1:
        return

    recur(idx + work[idx][0], price + work[idx][1])

    recur(idx, price)


N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
answer = 0

recur(0, 0)