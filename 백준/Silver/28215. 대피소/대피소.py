from itertools import combinations # 조합을 생성하기 위한 라이브러리리

def calculate_distance(house, shelter):
    # 두 좌표 간의 거리를 계산하는 함수
    return abs(house[0]-shelter[0]) + abs(house[1] - shelter[1])

def find_min_max_distance(N, K, houses):
    # 최적의 대피소 조합을 찾아 최소의 최대 거리를 반환하는 함수
    min_max_distance = float('inf') #초기값을 무한대로 설정(최소값을 찾기 위함)
    
    # 모든 가능한 대피소 조합을 생성 (houses 중 K개를 선택)
    for shelters in combinations(houses, K):
        max_distance = 0 # 현재 조합에서의 최대 거리 저장 변수
        
        # 모든 집에 대해 가장 가까운 대피소까지의 거리 계산
        for house in houses:
            min_distance = float('inf') # 현재 집에서 가장 가까운 대피소까지의 거리 초기화
            
            # 선택된 대피소들 중에서 가장 가까운 대피소 찾기
            for shelter in shelters:
                distance = calculate_distance(house, shelter) # 현재 집과 대피소 사이 거리 계산
                if distance < min_distance:
                    min_distance = distance # 최소 거리 갱신
            
            # 현재 조합에서 가장 멀리 떨어진 집의 거리 저장
            if min_distance > max_distance:
                max_distance = min_distance
            
        # 가능한 조합들 중 최소의 최대 거리 찾기
        if max_distance < min_max_distance:
            min_max_distance = max_distance
    return min_max_distance # 최적의 대피소 조합에 대한 최소의 최대 거리 반환


# 입력 처리
N, K = map(int, input().split()) # N:집의 개수, K: 대피소 개수
houses = [tuple(map(int, input().split())) for _ in range(N)] # 각 집의 (X, Y) 좌표를 리스트로 저장

# 결과 계산 및 출력
result = find_min_max_distance(N, K, houses)
print(result)
                