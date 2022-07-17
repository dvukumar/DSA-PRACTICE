class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        def permutation(nums,ind=0):
            if ind==len(nums):
                result.append(nums)
                return
            
            for i in range(ind,len(nums)):
                array = [c for c in nums]
                array[i],array[ind] = array[ind],array[i]
                permutation(array,ind+1)
        permutation(nums,0)
        return result