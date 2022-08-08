def solution(A, K):
    if len(A) == 0:
        return A
    for i in range(K):
        value = A.pop(len(A)-1)
        A = [value] + A
    return A

