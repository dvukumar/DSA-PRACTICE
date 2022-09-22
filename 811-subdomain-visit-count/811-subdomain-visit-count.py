class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dict = {}
        
        for domain in cpdomains:
            parts = domain.split(" ")
            num = int(parts[0])
            subDomain = parts[1]
            
            arr = subDomain.split(".")
            s = ""
            for string in reversed(arr):
                if len(s)==0:
                    s+=string
                    
                else:
                    s = string+"."+s
                
                if s in dict:
                    dict[s]+=num
                else:
                    dict[s] = num
        res = []
        for key in dict.keys():
            s = str(dict[key])
            s = s + " " +key
            res.append(s)
        return res