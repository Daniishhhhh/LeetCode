class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        result = []
        for i in nums:
            result.append(i*i)
        result.sort()

        return result