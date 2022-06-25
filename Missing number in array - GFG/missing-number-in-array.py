#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum = n*(n+1)//2
        #print(product)
        arrSum = 0
        for i in range(n-1):
            arrSum+=array[i]
        
        #print(arrProduct)
        return sum-arrSum
#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends