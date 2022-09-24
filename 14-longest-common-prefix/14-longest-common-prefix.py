class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minSize = 201
        for s in strs:
            size = len(s)
            minSize = min(minSize,size)
        
        j = 0
        while(j<minSize):
            temp = strs[0][j]
            for i in range(1,len(strs)):
                if temp!=strs[i][j]:
                    return res
            res+=temp
            j+=1
        return res
            
