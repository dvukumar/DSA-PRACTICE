#User function Template for python3

class Solution:
    def minimumSquares(self, L, B):
        
        def hcf(x,y):
            while y:
                x,y = y,x%y
            return x
        k = hcf(L,B)
        n = (L*B)//(k*k)
        
        return n,k

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends