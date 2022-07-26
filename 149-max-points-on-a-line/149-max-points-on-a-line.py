class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slope = []
        if len(points)==1:
            return 1
        
        for i in range(len(points)):
            a = points.pop(i)
            dict = {}
            for j in range(len(points)):
                b = points[j]
                
                if a[1]==b[1]:
                    m = 10**7
                else:
                    m = (a[0]-b[0])/(a[1]-b[1])
                #print(a,b,m)
                if m in dict:
                    dict[m]+=1
                else:
                    dict[m] = 1
            values = list(dict.values())
            max_ = max(values)
            slope.append(max_)
            points.insert(i,a)
            
        
        
        #print(slope)
        # print(values)
        return max(slope)+1
        