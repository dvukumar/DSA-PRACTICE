#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        
        n = len(A)
        s = 0
        l = n-1
        
        while(s<=l):
            mid = (s+l)//2
            #print(mid)
            if A[mid]==key:
                return mid
            
            if key>=A[s]:
                if A[mid]>key:
                    l = mid-1
                else:
                    if A[mid]<A[s]:
                        
                        l = mid - 1
                    else:
                        s = mid+1
            else:
                if A[mid]<key:
                    s = mid+1
                else:
                    if A[mid]>A[l]:
                        s = mid+1
                    else:
                        l = mid-1
                
        return -1
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends