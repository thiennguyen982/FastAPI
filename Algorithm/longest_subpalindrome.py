class Solution:
    def isPalindrome(self, s : str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        output = s[0]
        for i in range(0, length, 1):
            for j in range(length, -1, -1):
                substr = s[i:j]
                if self.isPalindrome(substr) & (len(substr) > len(output)):
                    output = substr
        return output
