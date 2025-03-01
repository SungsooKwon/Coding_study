s = "()()"

def solution(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        else: # char == ')'
            if stack:
                 stack.pop()
            else:
                return False # 스택이 비었는데 ')'가 나온 경우
            
    return len(stack) == 0

solution(s)