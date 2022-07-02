class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9+7
        horizontalCuts.sort()
        verticalCuts.sort()
        h_diff = []
        
        for i in range(len(horizontalCuts)):
            if i==0:
                diff = abs(0-horizontalCuts[i])
                
            else:
                diff = abs(val - horizontalCuts[i])
            
            h_diff.append(diff)
            val = horizontalCuts[i]
        
        diff = abs(val-h)
        h_diff.append(diff)
        
        v_diff = []
        
        for i in range(len(verticalCuts)):
            if i==0:
                diff = abs(0-verticalCuts[i])
                
            else:
                diff = abs(val - verticalCuts[i])
            
            v_diff.append(diff)
            val = verticalCuts[i]
        
        diff = abs(val-w)
        v_diff.append(diff)
        #print(h_diff)
        #print(v_diff)
        
        res = []
        max_v = max(v_diff)
        max_ = 0
        for i in range(len(h_diff)):
            
            val = (h_diff[i]*max_v)
            #print(val)
            max_ = max(val,max_)
            #print(max_%mod)
                
        return max_%mod
        
        