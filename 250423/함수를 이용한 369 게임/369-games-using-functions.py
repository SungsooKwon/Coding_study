a, b = map(int, input().split())

# Please write your code here.

def solution(a, b):
    cnt = 0
    
    for i in range(a, b + 1):
        if i % 3 == 0 or any(d in str(i) for d in ['3', '6', '9']):
            cnt += 1
        

    return cnt


print(solution(a, b))