#----------------  Single LinkedList  --------------------



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) :
        self.head=None
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next        
        temp.next=new_node
    def add_after(self,data,x):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            if x==temp.data:
                break
            temp=temp.next
        else:
            print("x is not in the list") 
        new_node.next=temp.next       
        temp.next=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("lisgt is empty")
            return
        if self.head.data==x:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        while temp.next.next is not None:
            if x==temp.next.data:
                break
            temp=temp.next
        else:
            print("x is not in the list") 
        new_node.next=temp.next       
        temp.next=new_node   
    def show(self):
        temp=self.head
        if temp is None:
            print("list is empty")
        else:    
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next
            print()    
    def del_begin(self):
        if self.head is None:
            print("list is already empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next 

    def del_end(self):
        if self.head is None:
            print("list is already empty")
            return     
        if self.head.next is None:
            self.head=None    
        temp=self.head
        while temp.next.next is  not None:
            temp=temp.next    
        temp.next=None   

    def del_by_val(self,val):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data==val:
            self.del_begin()
            return
        temp=self.head
        while temp.next is not None:
            if temp.next.data==val:
                break
            temp=temp.next
        else:
            print("val is not in list")  
        if temp.next is None:
            self.del_end()          
        else:
            temp.next=temp.next.next






ll=sll()
ll.add_begin(2)
ll.add_end(10)
ll.add_begin(4)
ll.add_after(6,2)
ll.show()
ll.add_before(3,2)
ll.add_before(11,4)
ll.show()
ll.del_begin()
ll.show()
ll.del_end()
ll.show()
ll.del_by_val(2)
ll.show()


#-------------------------  Doubly Linkedlist  ---------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        pass    
        
                         
    