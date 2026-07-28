from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Works when nums values are in the range 0..100
        count = [0] * 102  # 0..101, we store frequency at index num+1

        for num in nums:
            count[num + 1] += 1

        for i in range(1, 102):
            count[i] += count[i - 1]

        return [count[num] for num in nums]
