def myAtoi(s: str) -> int:
    s = s.replace(" ", "")
    result = ""
    start = None
    
    if not s[0].isdigit():
        return 0
    
    for char in s:
        if char.isdigit():
            start = s.index(char)
            break
        
    for i in range(start, len(s)):
        if s[i].isdigit():
            result += s[i]
        else:
            break
        
    return int(result) if s[start - 1] != "-" else int(result)*(-1)

if __name__ == "__main__":
    print(myAtoi("123456789"))
     
    for i in range(10, -1, -1):
        print(i)