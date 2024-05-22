
import ast

def find_longest_substring(str_1 : str, str_2 : str) -> str:
    len_1 = len(str_1)
    len_2 = len(str_2)
    
    dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]
    
    max_length = 0
    end_position = (0, 0)
    
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if str_1[i - 1] == str_2[j - 1]:
                print(str_1[i - 1], str_2[i - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length and str_1[i - dp[i][j] : i] == str_1[i - dp[i][j] : i][::-1]:
                    max_length = dp[i][j]
                    end_position = i 
                    
    res_string = str_1[end_position - max_length : end_position]
                    
    return res_string, max_length

if __name__ == "__main__":
    str_1 = "aaaaabbbbbfhlweaskufghbesldjkhfbkeashjcvkasdhjgv"
    str_2 = "udfhjgvbksdfjhvbksjdbvkjsdvaaaaabbbbbaisdkufbsdjklhfgbsdjklh"
    print(find_longest_substring(str_1, str_2))
