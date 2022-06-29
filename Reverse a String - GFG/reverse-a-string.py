#User function Template for python3

def reverseWord(s):
    n = len(s)
    i = 0
    j = n-1
    
    arr = []
    arr[:0] = s
    while(j>i):
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    
    s = "".join(arr)
    return s

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends