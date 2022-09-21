class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        Sum = nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            Sum = num+Sum
            if num>Sum:
                Sum = num
                dp[i] = num
                
            else:
                
              
                dp[i] = Sum
            maxSum = max(Sum,maxSum)
        #print(dp)
        return maxSum