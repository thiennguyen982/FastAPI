def solution(X, Y):
    max_path = 0
    X = sorted(set(X))
    steps = len(X) - 1
    for i in range(steps):
        temp_max = X[i + 1] - X[i]
        if temp_max >= max_path:
            max_path = temp_max
    return max_path, X

if __name__ == "__main__":
    print(solution(X=[4, 1, 5, 4, 8, 18], Y=[]))