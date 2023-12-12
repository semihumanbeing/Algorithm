def solution(s):
    dict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8, "nine":9}
    answer = ""
    a = 2
    for i in range(2, len(s)+2):
        if s[i - a].isdigit():
            answer += s[i-a]
            continue
        for j in range(5):
            if dict.get(s[i-2:i+j],'f') != 'f':
                answer += str(dict[s[i-2:i+j]])
                break
        
    print(answer)

solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("sixsix6")
solution("one0zero0")