class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        for num in nums:
            output += [lst+[num] for lst in output]
        return output