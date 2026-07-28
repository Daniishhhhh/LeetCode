class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in nums[i+1:]:
                j = nums.index(x, i+1)
                return [i, j]