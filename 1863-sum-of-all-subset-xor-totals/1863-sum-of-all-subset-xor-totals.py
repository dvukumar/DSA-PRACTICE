class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        arr = []
        s = []
        result = 0
        
        def subsets(s,i,nums):
            nonlocal result
            if i==len(nums):
                arr.append(list(s))
                subset_xor = 0
                for n in s:
                    subset_xor ^= n
                result += subset_xor
                return
                
            val = nums[i]
            s.append(val)
            subsets(s,i+1,nums)
            s.pop()
            subsets(s,i+1,nums)
        
        
                
        subsets(s,0,nums)
        print(arr)

        
        return result