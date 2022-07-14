#User function Template for python3

def count(n):
    table = [0]*(n+1) 
    table[0] = 1
        
    for i in range(3,n+1):
        table[i]+=table[i-3]
    #print(table)
    for i in range(5,n+1):
        table[i]+=table[i-5]
    #print(table)
    for i in range(10,n+1):
        table[i]+=table[i-10]
    #print(table)
    return table[n]

    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends