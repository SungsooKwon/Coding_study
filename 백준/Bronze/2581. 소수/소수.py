a = int(input())
b = int(input())
numbers = range(a, b + 1)

def is_prime(n):
    if n < 2: 
        return False  # 2보다 작은 수는 소수가 아님
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
        i += 1
    return True  # 소수이면 True 반환

total_sum = 0  # sum 함수와 이름 충돌 방지
mini = []

for num in numbers:
    if is_prime(num):  # 소수인지 확인
        mini.append(num)
        total_sum += num

if mini:  # 리스트가 비어있지 않으면
    print(total_sum)
    print(min(mini))  # 가장 작은 소수 출력
else:
    print(-1)  # 소수가 없을 경우 -1 출력
