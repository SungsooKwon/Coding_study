string = input().strip()
bomb = input().strip()

def solution(string, bomb):
    stack = []
    
    for char in string:
        stack.append(char) # 한 글자씩 추가
        
        # 스택의 끝부분이 폭발 문자열과 같은지 확인
        if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
            #  폭발 문자열이 있다면 제거
            for i in range(len(bomb)):
                stack.pop()
    
    # 결과 출력 (남은 문자열이 없다면 'FRULA')
    result = ''.join(stack)
    return result if result else "FRULA"

print(solution(string, bomb))