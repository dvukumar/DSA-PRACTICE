class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for curr in nums:
            if curr<=0:
                continue
            if curr-prev>1:
                return prev+1
            prev = curr
        if curr<0:
            return 1
        return curr+1
            