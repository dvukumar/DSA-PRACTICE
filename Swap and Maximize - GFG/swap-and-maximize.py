#User function Template for python3


def maxSum(arr,n):
    list = []
    arr.sort()
    i = 0
    while(i<n):
        val = arr.pop()
        if i%2==0:
            arr.append(val)
        else:
            arr.insert(i,val)
        i+=1
    
    #print(arr)
    res = abs(arr[0]-arr[-1])
    
    for i in range(1,len(arr)):
        res += abs(arr[i-1]-arr[i])
    
    return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int,input().split()))
    ans=maxSum(arr,n)
    print(ans)

# } Driver Code Ends