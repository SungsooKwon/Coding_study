from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

def solution(n, k, arr):
    freq = defaultdict(int) # 숫자의 등장 횟수 기록
    left = 0 # 왼쪽 포인터
    max_length = 0 # 최장 길이
    
    for right in range(n):
        freq[arr[right]] += 1
        
        while freq[arr[right]] > k: # 현재 숫자가 K번 초과 등장하면면
            freq[arr[left]] -= 1
            left += 1 # 왼쪽 포인터를 이동
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

print(solution(n, k, arr))