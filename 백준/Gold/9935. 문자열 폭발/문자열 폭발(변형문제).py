
#🧬 문제 설명
#DNA 실험 중 특정한 불안정 조각(BOMB) 이 감지되면 즉시 제거해야 한다.
#하지만 이번엔 제거된 위치 주변의 안정성도 고려해야 한다.

#당신은 아래와 같은 규칙으로 DNA 서열을 정제해야 한다.

# 📑 제거 규칙
# 문자열 S에서 BOMB와 일치하는 서열을 발견하면 즉시 제거한다.

# BOMB이 제거된 직후, 그 자리에 남아 있는 서열 중 SAFE가 있다면 절대 제거하지 않는다.

# 즉, SAFE 문자열은 폭발 영향으로 보호되며, 폭발 직후 그 영역에 BOMB이 있어도 제거되지 않는다.

# 위 과정을 더 이상 제거할 수 없을 때까지 반복한다.


# 📤 출력
# 모든 제거 작업이 끝난 후의 문자열을 출력한다.

# 모든 문자열이 제거되면 "CLEAN"을 출력한다.

# 오답 노트
# flag 개념 기억하기 -> Flase와 True 
s = "AAAASAFEAAA"
bomb = 'AAA'
safe = 'SAFE'

# s가 AAA보단 길어야한다
# SAFE 이후 AAA는 제거 하지 않는다. (pop 종료)

def solution(s, bomb, safe):
    stack = []
    safe_found = False
    for char in s:
        stack.append(char)
        
        if len(stack) >= len(safe) and ''.join(stack[-len(safe):]) == safe:
            safe_found = True
            
        if not safe_found and len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
                for i in range(len(bomb)):
                    stack.pop()
                    
    result = ''.join(stack)
    return result if result else "CLEAN"

solution(s, bomb, safe)
            
