#User function Template for python3

def getMinMax( a, n):
    
    int_min = 10**12+1
    int_max = 0
    
    for i in range(n): 
        
        res = a[i]
        if res<int_min:
            int_min = res
        if res>int_max:
            int_max = res
    
    return (int_min,int_max)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends