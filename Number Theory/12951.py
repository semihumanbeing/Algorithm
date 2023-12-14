def solution(s):
    answer = ''
    s_list = list(map(str, s.split(' ')))
    for i in range(len(s_list)):
        answer += s_list[i].capitalize() +' '
    print(answer[:-1])

solution("3people   unFollowed me")