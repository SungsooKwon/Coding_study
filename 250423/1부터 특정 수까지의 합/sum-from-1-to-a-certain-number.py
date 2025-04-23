n = int(input())

# Please write your code here.
def solution(n):
    return sum([i for i in range(1, n+1)]) // 10

print(solution(n))