class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if n==1:
                return n
            else:
                return -1
        val = trust[0][1]
        dict1 = {}
        dict2 = {}
        for edge in trust:
            val1 = edge[1]
            val2 = edge[0]
            if val1 in dict1:
                dict1[val1]+=1
            else:
                dict1[val1] = 1
            
            if val2 in dict2:
                dict2[val2]+=1
            else:
                dict2[val2] = 1
        #print(dict)
        for key in dict1.keys():
            if key not in dict2.keys():
                if dict1[key]==n-1:
                
                    return key
        return -1