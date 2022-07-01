#User function Template for python3

'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

'''
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
'''

def reorderList(self):
    if (self.head==None or self.head.next==None):
        return
    # write code to reorder Nodes of Linked_List
    slow = head
    fast = head.next
    
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        
    second = slow.next
    slow.next = None
    
    prev = None
    curr = second
    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    second = prev
    first = head
    
    curr1 = first
    curr2 = second
    
    while(curr2):
        
        temp1 = curr1.next
        temp2 = curr2.next
        curr1.next = curr2
        curr2.next = temp1
        curr1 = temp1
        curr2 = temp2
    return first
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reorder_List = reorderList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reorder_List()
        lis.printList()

# } Driver Code Ends