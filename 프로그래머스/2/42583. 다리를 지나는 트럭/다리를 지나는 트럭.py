# 트럭 여러 대가 일차선 다리를 정해진 순으로 건넌다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return
# 다리 최대 트럭 = bridge_length / limit-weight / 다리에 완전히 오르지 않은 트럭의 무게는 무시
# 트 2 무 10 [7,4 5,6]

# 트럭 queue 으로 while 확인,
# 첫 트럭 popleft -> first 변수
# 첫 트럭 popleft()
# for i in range(2): # 0, 1
#   if first == limit:
#       time += 1
#   elif first + tw[i] <= limit:
#       time += len(i)

# queue = popleft()
# time += 1
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (길이만큼 0으로 초기화)
    tw = deque(truck_weights)
    total_weight = 0  # 현재 다리 위 트럭들의 무게 합

    while bridge:
        time += 1
        # 다리에서 트럭 하나 나감
        out = bridge.popleft()
        total_weight -= out

        if tw:
            # 다음 트럭이 다리에 올라갈 수 있는 경우
            if total_weight + tw[0] <= weight:
                truck = tw.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 트럭 못 올라가면 0 추가 (시간 흐름)

    return time
