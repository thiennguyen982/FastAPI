def solution(*args, **kwargs):
    S = args[0]
    hw = args[1]
    count = 0
    while hw:
        temp = 0
        for element in hw:
            if S >= element:
                S += element
                hw.remove(element)
                temp += 1
        if temp > 0:
            count += temp
        else:
            return count

if __name__ == "__main__":
    print(solution(2, [18, 2, 5, 14, 3]))