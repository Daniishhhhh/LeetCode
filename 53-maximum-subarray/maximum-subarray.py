class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=0

        for n in nums:
            if currentsum <0:
                currentsum=0

            currentsum+=n
            maxsum =max(maxsum, currentsum)
        return maxsum        