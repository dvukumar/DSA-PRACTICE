#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        arr = []
        #print(Items[0].value)
        for i in range(n):
            val = Items[i].value
            weight = Items[i].weight
            ratio = val/weight
            arr.append([val,weight,ratio])
            
        
        arr.sort(key = lambda x:x[2], reverse = True)
        res = 0
        for i in range(n):
            val = arr[i][0]
            weight = arr[i][1]
            
            if W<weight:
                res+=(val/weight)*W
                W = 0
            else:
                res+=val
                W-=weight
        return res
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends