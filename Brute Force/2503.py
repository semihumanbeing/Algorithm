TC = int(input())
hint = [list(map(int, input().split())) for _ in range (4)]

# strike 숫자가 정답에 포함이고 자리도 동일
# ball 숫자가 정답에 포함
answer = 0

for a in range(1, 10):
    for b in range (10):
        for c in range (10):
            if (a ==b or b == c or c == a) :
                continue

            cnt = 0
            for arr in hint:
                check = list(hint[0]) # ['1','2','3']
                strike = int(hint[1])
                ball = int(hint[2])

                strike_count = 0
                ball_count = 0

                #스트라이크 계산
                if (a == int(check[0])):
                    strike_count += 1
                if (b == int(check[1])):
                    strike_count += 1
                if (c == int(check[2])):
                    strike_count += 1
                

                #볼 계산
                if (a == int(check[1]) or a == int(check[2])):
                    ball_count += 1
                if (b == int(check[0]) or b == int(check[2])):
                    ball_count += 1
                if (c == int(check[0]) or c == int(check[1])):
                    ball_count += 1
                
                
                #매칭 여부 확인
                if (strike != strike_count):
                    break
                if (ball != ball_count):
                    break          

                cnt += 1

                if cnt == TC:
                    answer += 1
print(answer)