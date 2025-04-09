# 명함 지갑을 만드는 회사에서 지갑 크기 정함
# 모든 명함의 가로 - 세로 길이를 나타내는 sizes

def solution(sizes):
    rotated = [(max(w, h), min(w, h)) for w, h in sizes]
    max_w = max(w for w, h in rotated)
    max_h = max(h for w, h in rotated)
    return max_w * max_h
