def dfs(numbers, target, index, total):
    if index == len(numbers):
        return 1 if total == target else 0
    
    return dfs(numbers, target, index + 1, total + numbers[index]) + \
           dfs(numbers, target, index + 1, total - numbers[index])


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
