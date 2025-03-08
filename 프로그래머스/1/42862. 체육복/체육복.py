# 학생 번호 = 체격 순
# 앞번호 학생이나 바로 뒷 번호의 학생에게만 체육복을 빌려 줄 수 있다.
# 4번 -> 3번, 5번 / 체육복을 적절히 빌려 최대한 많은 학생이 체육 수업을 들어야 한다.
# 전체 학생 수 n, 
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
# 여벌 학생 reserve,
# 체육수업을 들을 수 있는 학생의 최대값을 return
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):

    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 초기 체육 수업 가능 인원
    answer = n - len(lost_set)

    # 체육복 빌려주기
    for l in sorted(lost_set): # 정렬해서 앞번호 먼저 체크
        if l - 1 in reserve_set: # 앞 번호 학생이 여벌을 가지고 있으면
            reserve_set.remove(l - 1)
            answer += 1
        elif l + 1 in reserve_set: # 뒷 번호 학생이 여벌을 가지고 있으면
            reserve_set.remove(l + 1)
            answer += 1
    
    return answer

solution(n, lost, reserve)
