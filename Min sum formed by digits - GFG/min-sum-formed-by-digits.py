
class Solution:
    def minSum(self, arr, n):
        arr.sort()
        n1 = 0
        n2 = 0
        for i in range(len(arr)):
            if i%2==0:
                n1 = n1*10+arr[i]
            else:
                n2 = n2*10+arr[i]
        
        return n1+n2

#{ 
#  Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends