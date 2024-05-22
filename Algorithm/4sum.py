from itertools import combinations
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        result = []
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         for k in range(j + 1, length):
        #             for h in range(k + 1, length):
        #                 sum_ = nums[i] + nums[j] + nums[k] + nums[h]
        #                 if sum_ == target and ([nums[i], nums[j], nums[k], nums[h]] not in result):
        #                     result.append([nums[i], nums[j], nums[k], nums[h]])
        index_combinations = list(combinations(range(length), 4))
        for comb in index_combinations:
            if sum([nums[index_] for index_ in comb]) == target and [nums[index_] for index_ in comb] not in result:
                result.append([nums[index_] for index_ in comb])
        return result