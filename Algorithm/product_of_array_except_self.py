class Solution:
    def product_of_elements(self, nums):
        result = 1
        for num in nums:
            result *= num
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        for i in range(length):
            temp_nums = nums[:i] + nums[i+1:]
            result.append(self.product_of_elements(temp_nums))
        return result