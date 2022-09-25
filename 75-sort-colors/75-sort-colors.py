class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        while(j<n):
            if nums[i]==0:
                val = nums.pop(i)
                nums.insert(0,val)
                i+=1
            elif nums[i]==2:
                val = nums.pop(i)
                nums.append(val)
            else:
                i+=1
            j+=1