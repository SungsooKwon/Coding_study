import math

room_number = input() # 입력 받기
count = [0] * 10 # 0 ~ 9 까지 숫자 개수 지정

# 숫자 개수 세기
for digit in room_number:
    count[int(digit)] += 1

# 6과 9를 합쳐서 계산 (2로 나누고 올림)
count[6] = count[9] = math.ceil((count[6] + count[9]) / 2)

print(max(count))
