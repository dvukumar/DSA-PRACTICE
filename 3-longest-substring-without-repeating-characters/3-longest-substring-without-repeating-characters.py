class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        n = len(s)
        arr = []
        j = 0
        i = 0
        while(i<n):
            char = s[i]
            if char not in string:
                string = string+char
                i+=1
                
            else:
                arr.append(string)
                
                j = string.index(char)+1
                #print(j)
                string = string[j:]+char
                i+=1
        arr.append(string)
        #print(arr)
        substring = max(arr,key = len)
        #print(substring)
        return len(substring)