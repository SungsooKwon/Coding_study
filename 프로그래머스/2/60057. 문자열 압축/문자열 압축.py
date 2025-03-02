def solution(s):
    if len(s) == 1:
        return 1
    
    min_length = float('inf')  # 최소 길이를 저장할 변수
    
    for step in range(1, len(s) // 2 + 1):  # 압축 단위를 1부터 N/2까지 변경
        compressed = ""  # 압축된 문자열을 저장
        prev = s[:step]  # 초기 부분 문자열
        count = 1  # 반복 횟수

        for i in range(step, len(s), step):  # step 간격으로 반복
            if s[i:i+step] == prev:  # 이전 문자열과 같으면 카운트 증가
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[i:i+step]  # 새로운 비교 문자열 설정
                count = 1  # 카운트 초기화
        
        compressed += str(count) + prev if count > 1 else prev  # 마지막 문자열 처리
        
        min_length = min(min_length, len(compressed))  # 최소 길이 갱신
    
    return min_length
print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17