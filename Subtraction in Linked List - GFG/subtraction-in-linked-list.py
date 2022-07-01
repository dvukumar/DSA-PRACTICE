#User function Template for python3

def subLinkedList(l1, l2): 
    # Code here
    # return head of difference list
    num1 = 0
    curr1 = l1
    n1 = 0
    while(curr1):
        val = curr1.data
        num1 = num1*10+val
        curr1 = curr1.next
        n1+=1
    
    num2 = 0
    curr2 = l2
    n2 = 0
    
    while(curr2):
        val = curr2.data
        num2 = num2*10+val
        curr2 = curr2.next
        n2+=1
    
    diff = str(abs(num1-num2))
    n = len(diff)
    if n1>n2:
        head = l1
        res = l1
    else:
        head = l2
        res = l2
    i = 0
    prev = None
    while(i<n):
        val = int(diff[i])
        head.data = val
        prev = head
        head = head.next
        i+=1
    
    prev.next = None
    
    return res
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends