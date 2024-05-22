from typing import List

def removeElement(nums: List[int], val: int) -> int:
    result = []
    for num in nums:
        if num != val:
            result.append(num)
    return len(result)

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    
    print(removeElement(nums, val))