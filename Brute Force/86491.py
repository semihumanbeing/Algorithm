def solution(sizes):
    answer = 0
    w = 0
    h = 0
    sortedSizes = []
    # 리스트를 각각 정렬
    for i in range(len(sizes)):
        sortedSizes.append(sorted(sizes[i]))
    
    for j in range(len(sizes)):
        w = max(w, sortedSizes[j][0])
        h = max(h, sortedSizes[j][1])

    print(w)
    print(h)

    # 가장큰 가로와 가장 큰 세로를 곱한결과
    

    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))