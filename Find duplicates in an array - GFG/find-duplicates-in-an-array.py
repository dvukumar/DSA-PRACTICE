class Solution:
    def duplicates(self, arr, n): 
    	# code here
        arr0 = []
        arr.sort()
        flag = False
        for i in range(n-1):
            a1 = arr[i]
            a2 = arr[i+1]
            if a1==a2:
                val = a1
                flag = True
            else:
                if flag==True:
                    arr0.append(val)
                    flag = False
                else:
                    continue
        if flag==True:
            arr0.append(val)
        if len(arr0)==0:
            return [-1]
        else:
            return arr0
            
        
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends