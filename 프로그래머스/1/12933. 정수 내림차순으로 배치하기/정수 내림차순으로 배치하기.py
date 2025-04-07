def solution(n):
    str_n = str(n)

    numbers = sorted(str_n, reverse=True)
        
    return int("".join(numbers))