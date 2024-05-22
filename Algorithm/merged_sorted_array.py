from typing import List

def mergeSortedArray(list1 : List[int], list2 : List[int]) -> List[int]:
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1[0])
            list1 = list1[1:]
        else:
            result.append(list2[0])
            list2 = list2[1:]
    if list1:
        result.extend(list1)
    else:
        result.extend(list2)
    return result

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    return mergeSortedArray(nums1, nums2)

if __name__ == "__main__":
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    
    nums2 = [2,5,6]
    n = 3
    
    print(merge(nums1, m, nums2, n))