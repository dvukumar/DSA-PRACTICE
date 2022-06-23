class Solution:
    def isValid(self, s: str) -> bool:
        
        arr = []
        for i in range(len(s)):
            char = s[i]
            n = len(arr)
            if n==0 and (char==')' or char=='}' or char==']'):
                return False
            elif char=='(' or char=='{' or char=='[':
                arr.append(char)
            elif char==')':
                if arr[-1]=='(':
                    arr.pop()
                else:
                    return False
            elif char=='}':
                if arr[-1]=='{':
                    arr.pop()
                else:
                    return False
            elif char==']':
                if arr[-1]=='[':
                    arr.pop()
                else:
                    return False
            else:
                return False
        
        return len(arr)==0