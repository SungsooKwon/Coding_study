def solution(x):
    if x % sum([int(s) for s in str(x)]) == 0:
        return True
    else:
        return False