class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        result = []
        def CombinationSum(target,i,temp):
            if target==0:
                result.append(temp)
                return
            if target<0 or i>=n:
                return
            
            CombinationSum(target-candidates[i],i,temp+[candidates[i]])
            CombinationSum(target,i+1,temp)
        CombinationSum(target,0,[])
        return result