class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        j = 0
        while(i<n):
            num = nums[j]
            if num==0:
                nums.append(nums.pop(j))
            else:
                j+=1
            
            i+=1
        
                