class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)
        dp1 = [0 for _ in range(n-1)]
        dp2 = [0 for _ in range(n-1)]
        
        dp1[0] = nums[0]
        dp1[1] = max(nums[0],nums[1])
        
        dp2[0] = nums[1]
        dp2[1] = max(nums[1],nums[2])
        
        for i in range(2,n-1):
            dp1[i] = max(dp1[i-2]+nums[i],dp1[i-1])
        
        for i in range(3,n):
            dp2[i-1] = max(dp2[i-3]+nums[i],dp2[i-2])
        
        return max(dp1[-1],dp2[-1])
            
                