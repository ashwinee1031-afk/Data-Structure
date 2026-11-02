#wap to count occurence of a number in the doubly linkedlist
class node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node
    def print(self):
        temp=self.head
        print("list element :")
        while temp:
            print(temp.data)
            temp=temp.next
    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=temp
            self.head.prev=new_node
            self.head=new_node
            
        else:
            p=1
            while (p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            if temp.next:
                temp.next.prev=new_node
            temp.next=new_node
            new_node.prev=temp
            # temp.next=new_node
            # new_node.prev=temp
            # new_node.next=temp.next
            if temp.next:
                temp.next.prev=new_node

    def reverse(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        while (temp):
            print(temp.data)
            temp=temp.prev
    # doubly linear linked list
    def delete(self,value):
        temp=self.head
        if temp.data ==value:
            self.head=self.head.next
            self.head.prev=None
        else:
            while (temp.data!=value and temp):
                temp=temp.next
                if temp==None:
                    print("value is not present in list")
                    return 
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.next
            temp=None

    def count_occ(self,num):
        temp=self.head
        cnt=0
        while temp:
            if temp.data==num:
                cnt+=1
            temp=temp.next
        print("the occurence: ",cnt)


list=linkedlist()
list.append(node(10))
list.append(node(20))
list.append(node(10))
list.append(node(30))
list.insert(node(25),3)
# list.reverse()
list.delete(20)
list.count_occ(10)
list.print()
