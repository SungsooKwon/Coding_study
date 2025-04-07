def solution(n):
    str_n = str(n)
    numbers = []
    for i in range(len(str_n)):
        numbers.append(str_n[i])
    numbers = sorted(numbers, reverse=True)
        
    return int("".join(numbers))