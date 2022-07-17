class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #nums.sort()
        result = []
        
        def permutation(nums,ind):
            if ind==len(nums):
                if nums not in result:
                    result.append(nums)
                return
            prev = -11
            for i in range(ind,len(nums)):
                if prev==nums[i]:
                    continue
                
                array = [c for c in nums]
                
                array[i],array[ind] = array[ind],array[i]
                permutation(array,ind+1)
                prev = nums[i]
                
        permutation(nums,0)
        return result