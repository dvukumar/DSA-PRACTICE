class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        
        i = 0
        res = 0
        while(i<len(parts1) and i<len(parts2)):
            num1 = int(parts1[i])
            num2 = int(parts2[i])
            if num1>num2:
                return 1
            elif num2>num1:
                return -1
            else:
                res = 0
            i+=1
        
        if i<len(parts1):
            while(i<len(parts1)):
                num = int(parts1[i])
                i+=1
                if num>0:
                    return 1
            return 0
        
        if i<len(parts2):
            while(i<len(parts2)):
                num = int(parts2[i])
                i+=1
                if num>0:
                    return -1
            return 0
        return res
            
            
    