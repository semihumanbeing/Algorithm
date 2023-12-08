N, M = map(int, input().split())
arr = []

def rec(number):
    # 숫자가 M 이 되었을때 출력하고 탈출
    if number == M:
        print(*arr)
        return
    
    # 1부터 N까지 수열 데이터를 저장
    for i in range(1, N+1):
        arr.append(i)
        rec(number+1)
        arr.pop()


rec(0)