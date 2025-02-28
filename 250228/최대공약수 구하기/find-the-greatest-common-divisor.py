n, m = map(int, input().split())

data = []

# Please write your code here.
for i in range(1, n + 1):
    if (n % i == 0) and (m % i == 0):
        data.append(i)
        gcd = i

print(gcd)