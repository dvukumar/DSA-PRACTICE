class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        arr = []
        s = []
        result = 0
        
        def subsets(s,i,nums,arr):
            nonlocal result
            if i==len(nums):
                arr.append(s)
                subset_xor = 0
                for n in s:
                    subset_xor ^= n
                result += subset_xor
                return
                
            val = nums[i]
            s.append(val)
            subsets(s,i+1,nums,arr)
            s.pop()
            subsets(s,i+1,nums,arr)
        
        
                
        subsets(s,0,nums,arr)
        print(arr)
        
        return result