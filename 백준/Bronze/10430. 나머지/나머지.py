# 입력 받기
A, B, C = map(int, input().split())

# 결과 계산
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
