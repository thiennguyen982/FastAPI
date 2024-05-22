def solution(A):
    if len(A) == 1:
        return 1
    current_even, current_odd = A[0], A[1]
    start, max_len = 0, 0
    for i in range(2, len(A)):
        if (i % 2 == 0 and A[i] != current_even) or (i % 2 == 1 and A[i] != current_odd):
            max_len = max(max_len, i - start)
            start = i - 1
            if i % 2 == 0:
                current_even, current_odd = A[i], A[i - 1]
            else:
                current_even, current_odd = A[i - 1], A[i]
    return max(max_len, len(A) - start)


if __name__ == "__main__":
    print(solution([3, 2, 3, 2, 3]))