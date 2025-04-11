# 올바른 괄호 문자열인지 확인하는 함수
def is_correct(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:  # ')'인 경우
            if not stack:  # 스택이 비었으면 짝이 안 맞음
                return False
            stack.pop()  # '(' 하나 꺼내서 짝 맞춰줌
    return not stack  # 스택이 비어있으면 올바른 괄호

# 메인 함수
def solution(p):
    # 1. 입력이 빈 문자열이면 빈 문자열 반환
    if p == "":
        return ""

    # 2. 문자열을 균형잡힌 괄호 문자열 u, v로 분리
    open_count, close_count = 0, 0
    for i in range(len(p)):
        if p[i] == '(': open_count += 1
        else: close_count += 1
        # 처음으로 괄호 수가 같은 지점에서 자름
        if open_count == close_count:
            u = p[:i+1]  # 앞부분
            v = p[i+1:]  # 뒷부분
            break

    # 3. u가 올바른 괄호 문자열이면 v에 대해 재귀 수행 후 붙이기
    if is_correct(u):
        return u + solution(v)

    # 4. u가 올바르지 않으면
    else:
        # ( + solution(v) + ) 를 기본으로 하고
        new_str = "("
        new_str += solution(v)
        new_str += ")"
        # u의 첫 번째와 마지막 문자 제거 후 나머지 문자 뒤집기
        for char in u[1:-1]:
            if char == '(':
                new_str += ')'
            else:
                new_str += '('
        return new_str
