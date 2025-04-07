# solution -> x, n 
# x 부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트
def solution(x, n):
    return [x + x * i for i in range(n)]