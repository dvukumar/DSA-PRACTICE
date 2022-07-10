#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        arr = []
        for i in range(n):
           
            arr.append([start[i],end[i]])
        
        arr.sort(key = lambda x:x[1])
        #print(arr)
        
        s0 = arr[0][0]
        e0 = arr[0][1]
        count = 1
        for i in range(1,len(arr)):
            s = arr[i][0]
            e = arr[i][1]
            
            if s>e0:
                s0 = s
                e0 = e
                count+=1
        #print(arr)
        return count
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends