#singly linear linked list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
           self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node #appending new node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)      
            temp=temp.next
l1=LinkedList()
n1=Node(10)
n2=Node(20)       
n3=Node(30)
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(Node(40))
l1.display()