#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(Parr, n):
    
    arr = []
    for i in range(n):
        a = Parr[i].a
        b = Parr[i].b
        
        arr.append([a,b])
    
    arr.sort(key = lambda x:x[1])
    #print(arr)
    count = 1
    val1 = arr[0][1]
    for i in range(1,n):
        val2 = arr[i][0]
        if val2>val1:
            count+=1
            val1 = arr[i][1]
    
    if count==0:
        count+=1
    return count
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends