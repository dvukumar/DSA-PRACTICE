class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dict = {}
        
        for word in words:
            s = ""
            for char in word:
                i = ord(char) - ord('a')
                s+=arr[i]
            if s in dict:
                dict[s]+=1
            else:
                dict[s] = 1
        
        keys = list(dict.keys())
        return len(keys)