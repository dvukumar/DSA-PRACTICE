class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr)<=k:
            return arr
        i = 0
        j = len(arr)-1
        ans = []
        while(i<j):
            num1 = arr[i]
            num2 = arr[j]
            
            diff1 = abs(num1-x)
            diff2 = abs(num2-x)
            
            if diff1<diff2:
                ans.append([diff1,num1])
                i+=1
            elif diff1>diff2:
                ans.append([diff2,num2])
                j-=1
            else:
                if num1<num2:
                    ans.append([diff1,num1])
                    i+=1
                else:
                    ans.append([diff2,num2])
                    j-=1
        ans.sort()
        res = []
        for i in range(k):
            val = ans[i][1]
            res.append(val)
        res.sort()
        return res
        
        