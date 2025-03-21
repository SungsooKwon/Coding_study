def solution(name):
    answer = 0
    n = len(name)

    # 1. 알파벳 변경 최소 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 2. 커서 이동 최소 횟수 계산
    move = n - 1  # 일단 오른쪽으로 쭉 가는 경우

    for i in range(n):
        next_idx = i + 1
        # 연속된 A 구간 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        # 왼쪽으로 갔다가 오른쪽으로 가는 경우 vs 그냥 오른쪽으로만
        move = min(move, i + i + (n - next_idx))
        move = min(move, i + 2 * (n - next_idx))  # 오른쪽 끝 먼저 간 다음 왼쪽으로

    answer += move
    return answer
