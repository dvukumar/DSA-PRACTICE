class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dic:
                list = dic[key]
                list.append(s)
                dic[key] = list
            else:
                list = []
                list.append(s)
                dic[key] = list
        return dic.values()