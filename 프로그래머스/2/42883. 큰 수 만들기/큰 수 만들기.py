def solution(number, k):
    stack = []

    for num in number:
        # 앞의 숫자가 더 작으면 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 남은 k만큼 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
