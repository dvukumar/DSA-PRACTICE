class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(arr,i,curr):
            if i==len(arr):
                result.append(curr)
                return
            
            dfs(arr,i+1,curr+[arr[i]])
            dfs(arr,i+1,curr)
        dfs(nums,0,[])
        return result