# User function Template for Python3

# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        
        odd_node = head
        even_node = None
        
        curr = odd_node
        prev = None
        start_node = None
        while(curr):
            val = curr.data
            if val%2==0:
                if prev is None:
                    next = curr.next
                    #curr.next = None
                    
                    odd_node = next
                    if even_node is None:
                        even_node = curr
                        start_node = even_node
                    else:
                        even_node.next = curr
                        even_node = even_node.next
                    curr = next
                else:
                    next = curr.next
                    prev.next = next
                    #curr.next = None
                    if even_node is None:
                        
                        even_node = curr
                        start_node = even_node
                    else:
                        even_node.next = curr
                        even_node = even_node.next
                    curr = next
            else:
                next = curr.next
                prev = curr
                curr = next
                
        if start_node is None:
            return odd_node
        elif odd_node is None:
            return start_node
        even_node.next = odd_node
        return start_node
        
                    

#{ 
#  Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(n, list1.head)
        printlist(newhead)


# } Driver Code Ends