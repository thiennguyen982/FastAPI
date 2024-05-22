import time

def fix_potholes(S):
    fixed_section = 0
    
    for i in range(len(S)):
        if S[i] == "X":
            S = S[i:]
            break
        
    while S:
        temp_s = S[0:3]
        if "X" in temp_s:
            fixed_section += 1
        S = S[3:]

    return fixed_section

if __name__ == "__main__":
    S = "............XXXXXXXXXXXX......XXXXXXXXXXXXXX.........."
    solution = fix_potholes(S)

    print(solution)
