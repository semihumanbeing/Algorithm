def solution(triangle):
    answer = []
    
    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
            
    print(triangle)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
