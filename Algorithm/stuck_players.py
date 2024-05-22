def solution(S):
    result = 0
    S = " " + S + " "
    S_list = list(S)

    steps = len(S_list)
    
    for i in range(1, steps):
        if S_list[i] == "v" or S_list[i] == "^":
            result += 1
            S_list[i] = " "
        if S_list[i] == ">" and S_list[i + 1] == " ":
            result += 1
            S_list[i] = " "
        if S_list[i] == "<" and S_list[i - 1] == " ":
            result += 1
            S_list[i] = " "
            
    return result

print(solution("><^v"))