#https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U', '']
    dict = []
    
    for a1 in chars[0:5]:
        dict.append(a1)

    for a1 in chars[0:5]:
        for a2 in chars[0:5]:
            dict.append(a1+a2)
            
    for a1 in chars[0:5]:
        for a2 in chars[0:5]:
            for a3 in chars[0:5]:
                dict.append(a1+a2+a3)
                
    for a1 in chars[0:5]:
        for a2 in chars[0:5]:
            for a3 in chars[0:5]:
                for a4 in chars[0:5]:
                    dict.append(a1+a2+a3+a4)
                    
    for a1 in chars[0:5]:
        for a2 in chars[0:5]:
            for a3 in chars[0:5]:
                for a4 in chars[0:5]:
                    for a5 in chars[0:5]:
                        dict.append(a1+a2+a3+a4+a5)
    
    dict.sort()
    
    return dict.index(word)+1


print(solution("AAAAE")) #6
print(solution("AAAE")) #10
print(solution("I")) #1563
print(solution("EIO")) #1189