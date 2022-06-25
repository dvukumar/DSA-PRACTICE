class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        n = 0
        while(n<l):
            if nums[i]==val:
                nums.pop(i)
                n+=1
            else:
                i+=1
                n+=1
            
        print(nums)
        return len(nums)