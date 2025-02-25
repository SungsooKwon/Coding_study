n = int(input())
b = list(map(int, input().split()))

def solution(n):
    if n < 2: 
        return False # 2보다 작은 수는 소수가 아님
    i = 2
    while i * i <= n: # 루트 2 대신 i * i 사용
        if n % i == 0:
            return False # 나누어 떨어지면 소수가 아님
        i += 1
        
    return True

count = 0 
for num in b:
    if solution(num):
        count +=1
        
print(count)    