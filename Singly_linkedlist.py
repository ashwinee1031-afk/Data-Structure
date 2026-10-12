#inserting new node into singly linkedlist
#find out middle node and also delete first and last node.
#delete alternate node from this.

# singly linear linked list
#deletion and reverse of node in linkedlist
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    def insert(self, new_node, pos):
        temp = self.head

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        p = 1

        while p != pos - 1:
            temp = temp.next
            p += 1

        new_node.next = temp.next
        temp.next = new_node

    def delete(self, val):
        temp = self.head

        # If list is empty
        if temp == None:
            print("List is empty")
            return

        # Deleting first node
        if temp.data == val:
            self.head = self.head.next
            return

        # Search for the node
        while temp:
            if temp.data == val:
                break

            prev = temp
            temp = temp.next

        # Value not found
        if temp == None:
            print("Value is not there in list")
            return

        # Delete node
        prev.next = temp.next

    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev


    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    
    def findmid_delete(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("middle node",temp.data)
        prev.next=temp.next
        temp=None

    

    def deletefirst_last(self, position):
        if self.head is None:
            print("Linked list is empty")
            return
        if position == "first":
            self.head = self.head.next
            return
        if position == "last":
            if self.head.next is None:
                self.head = None
                return
            temp = self.head
            while temp.next.next is not None:
                    temp = temp.next

    
    def delete_alternate_nodes(self):
        # temp = self.head
        # while temp and temp.next:
        #     # Delete the next node
        #     temp.next = temp.next.next
        #     # Move to the next node that is kept
        #     temp = temp.next

                    #OR

        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next



list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(50)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(40))

list.insert(Node(100), 1)
list.insert(Node(66), 4)
list.insert(Node(80), 7)
list.insert(Node(99), 9)
list.delete(30) #delete
# list.delete(1023)
# list.head = list.reverse()  #reverse
list.print()
list.deletefirst_last(1)
list.delete_alternate_nodes()
list.print()