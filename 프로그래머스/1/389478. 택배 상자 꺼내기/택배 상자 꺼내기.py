def solution(n, w, num):
    pos = {}  # 상자 번호를 키로 하고 (층, 열)을 값으로 저장하는 딕셔너리

    # 상자 번호 1번부터 n번까지 하나씩 위치 계산
    for i in range(n):
        box_num = i + 1              # 상자 번호는 1번부터 시작
        layer = i // w               # 현재 상자가 위치한 층 (0층부터 시작)
        index_in_layer = i % w       # 해당 층에서 몇 번째 위치에 놓이는지

        if layer % 2 == 0:
            col = index_in_layer     # 짝수 층은 왼쪽 → 오른쪽으로 쌓음
        else:
            col = w - 1 - index_in_layer  # 홀수 층은 오른쪽 → 왼쪽으로 쌓음

        pos[box_num] = (layer, col)  # 상자의 위치를 딕셔너리에 저장

    # 꺼내고자 하는 상자의 위치를 확인
    target_layer, target_col = pos[num]

    count = 0  # 꺼내야 하는 상자의 총 개수를 저장할 변수

    # num번 상자부터 n번 상자까지 반복하며 위에 쌓인 상자를 확인
    for b in range(num, n + 1):
        layer, col = pos[b]
        # 꺼내려는 상자 위에 있고 같은 열에 위치한 경우 개수 증가
        if col == target_col and layer >= target_layer:
            count += 1

    return count  # 꺼내야 하는 상자의 총 개수 반환
