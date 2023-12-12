candy = int(input())

# 남는 사탕이 없어야 한다
# A 는 B 보다 2개 이상 많은 사탕을 가져야 한다
# 셋 중 사탕을 못받는 친구는 없어야 한다
# C 가 받는 사탕은 짝수이다

answer = 0

for A in range(0, candy + 1):
    for B in range(0, candy + 1):
        for C in range(0, candy + 1):
            if A + B + C == candy:
                if A >= B+2:
                    if A !=0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            answer += 1

print(answer)