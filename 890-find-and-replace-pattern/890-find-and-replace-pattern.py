class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def find(dict,word,pattern):
            s = ""
            for i in range(len(word)):
                a = word[i]
                b = pattern[i]
                if a in dict:
                    if dict[a]==b:
                        s+=b
                    else:
                        return False
                else:
                    dict[a] = b
                    s+=b
            return s==pattern
                
        
        res = []
        for word in words:
            if find({},word,pattern) and find({},pattern,word):
                res.append(word)
        return res