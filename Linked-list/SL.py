class LinkedList:
    temp.next = new_node
def append(self,new_node):
    temp = temp.next
def insert(self,new_node,pos):
    if pos == 1:
        new_node.new_node=self.head
        self.head=new_node
    else:
        while(p!=pos-1):
            temp=temp.next
            p+=1
        new_node.next=temp.next
        temp.next=new_node                
    