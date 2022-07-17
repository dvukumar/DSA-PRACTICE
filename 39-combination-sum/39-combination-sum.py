class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        result = []
        
        def find_combs(target,temp,i):
            if target==0:
                result.append(list(temp))
                return
            if i==n or target<0:
                return
            
            find_combs(target-candidates[i],temp + [candidates[i]],i)
            find_combs(target,temp ,i+1)
        find_combs(target,[],0)
        return result
            
                