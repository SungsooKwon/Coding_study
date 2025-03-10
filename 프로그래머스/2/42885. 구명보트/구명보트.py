from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    boat = 0

    while people:
        # 가장 무거운 사람을 태움
        heavy = people.pop()
        
        # 가장 가벼운 사람과 함께 탈 수 있는지 확인
        if people and heavy + people[0] <= limit:
            people.popleft()
        
        boat += 1

    return boat