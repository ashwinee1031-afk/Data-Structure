#inserting new node into singly linkedlist

class LinkedList:
    temp.next = new_node
def append(self,new_node):
    temp = temp.next
def insert(self,new_node,pos):
    temp=self.head
    if pos == 1:
        new_node.new_node=self.head
        self.head=new_node
    else:
        p=1
        while(p!=pos-1):
            temp=temp.next
            p+=1
        new_node.next=temp.next
        temp.next=new_node
def display(self):
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next.next
        if temp:
            print(temp.data)
l1=LinkedList()
n1=Node(10)
n2=Node(20)       
n3=Node(30)
n4=Node(40)
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
l1.append(Node(-40))
l1.insert()

l1.display()    