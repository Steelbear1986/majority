from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for v, k in nums.items():
            if k == max(nums.values()): return v
