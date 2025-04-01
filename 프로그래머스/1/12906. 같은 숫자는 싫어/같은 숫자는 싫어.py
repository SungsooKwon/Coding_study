# 배열 arr이 주어짐
# 각 원소는 숫자 0 ~ 9 
# 연속적으로 나타나는 숫자를 하나만 남기고 제거
# 단, 제거된 후 남음 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지 (sort 금지)

arr = [1,1,3,3,0,1,1]

def solution(arr):
    stack = []
    for s in arr:
        if stack and stack[-1] == s: # 스택 안에 같은 숫자가 있다면?
            continue
        stack.append(s)
    return stack
    
solution(arr)