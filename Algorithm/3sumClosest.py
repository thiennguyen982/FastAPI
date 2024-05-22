from itertools import combinations

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        index_combinations = list(combinations(range(len(nums)), 3))
        ref = float('inf')
        res_sum = 0
        for comb in index_combinations:
            elements = [nums[index_] for index_ in comb]
            temp_sum = sum(elements)
            gap = abs(temp_sum - target)
            if gap < ref:
                ref = gap
                res_sum = temp_sum
        return res_sum