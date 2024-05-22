from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    strs.sort()
    steps = len(strs[0])
    for i in range(steps):
        first_queue = [str_[0] for str_ in strs]
        if len(set(first_queue)) == 1:
            result += first_queue[0]
            strs = [str_[1:] for str_ in strs]
        else:
            return result