# 행과 열 크기가 같은 두 행렬
# 두 행렬의 같은 행, 열 값을 서로 더한 값
# 
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1