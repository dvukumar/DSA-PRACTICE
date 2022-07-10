#User function Template for python3

class Solution:
    def minPartition(self, N):
        arr0 = [1,2,5,10,20,50,100,200,500,2000]
        arr0.sort(reverse = True) 
        count = 0
        a = []
        for i in arr0:
            x = N//i
            for j in range(x):
                a.append(i)
                N-=i
        return a
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends