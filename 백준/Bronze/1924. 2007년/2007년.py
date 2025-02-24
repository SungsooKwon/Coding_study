import datetime

# 입력 받기
month, day = map(int, input().split())

# 2007년 해당 날짜의 요일 찾기
date = datetime.date(2007, month, day)

# 요일 리스트 (0: 월요일 ~ 6: 일요일)
weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# 결과 출력
print(weekdays[date.weekday()])
