def solution(num):
    i = num
    cnt = 0
    lim = 0
    while(i != 1):
        if lim == 500:
            cnt = -1
            return cnt
        if i % 2 == 0:
            i = i / 2
            cnt += 1
            lim += 1
            continue
        if i % 2 == 1:
            i = i * 3 + 1
            cnt += 1
            lim += 1
    return cnt

num = 16
solution(num)