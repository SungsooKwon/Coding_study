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
            