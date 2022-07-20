class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def check(str1,str2):
            
            pos = -1
            for char in str2:
                pos = str1.find(char,pos+1)
                if pos==-1:
                    return False
            return True
        
        
            
        
        count = 0
        for word in words:
            result = check(s,word)
            if result:
                count+=1
        return count
                
                            