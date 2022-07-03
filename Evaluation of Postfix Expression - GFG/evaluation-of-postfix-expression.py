#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        arr = []
        
        n = len(S)
        #if n<=2:
            #return -1
        
        arr.append(S[0])
        arr.append(S[1])
        
        for i in range(2,n):
            char = S[i]
            if char=="+":
                item1 = arr.pop()
                item2 = arr.pop()
                
                res = int(item1)+int(item2)
                arr.append(res)
            
            elif char=="-":
                item1 = arr.pop()
                item2 = arr.pop()
                
                res = int(item2)-int(item1)
                arr.append(res)
            
            elif char=="/":
                item1 = arr.pop()
                item2 = arr.pop()
                
                res = int(item2)/int(item1)
                arr.append(res)
            
            elif char=="*":
                item1 = arr.pop()
                item2 = arr.pop()
                
                res = int(item1)*int(item2)
                arr.append(res)
            
            else:
                arr.append(char)
            #print(arr)
        
        return arr[0]
            
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends