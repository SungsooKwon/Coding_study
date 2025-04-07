# len('p') == len('y') -> True
# if not len('p') and len('y') -> True
# len('p') != len('y') -> False
def solution(s):
    sl = s.lower()
    if sl.count('p') == sl.count('y'):
        return True
    else:
        return False