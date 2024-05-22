import random
from typing import List, Dict

def solution(n : int) -> Dict[str, int]:
    
    parentheses_list = [('(' if i < n else ')') for i in range(2 * n)]
    result_list = {}
    
    def is_valid(input_str: str) -> bool:
        balance = 0
        for char in input_str:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    def solve(parentheses_list: List[str], current_result: str):
        if len(current_result) == 2 * n:
            if is_valid(current_result):
                result_list[current_result] = 1
            return
        for _ in range(2 * n - len(current_result)):
            random_index = random.randint(0, len(parentheses_list) - 1)
            random_element = parentheses_list.pop(random_index)
            solve(parentheses_list, current_result + random_element)
            parentheses_list.insert(random_index, random_element)

    parentheses_list = ['('] * n + [')'] * n
    solve(parentheses_list, "")
    
    return [key for key, value in result_list.items()]
    
if __name__ == "__main__":
    n = 5
    print(solution(n))
