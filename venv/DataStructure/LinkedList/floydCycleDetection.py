class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def inserAt(self,index,data):
        if self.head==None:
           self.head=Node(data)
           return
        itr=self.head
        count=1
        while(itr.next and count<=index):
            itr=itr.next
            count+=1
        itr.next=Node(data)

    def print(self):
        if self.head==None:
            print("List is Empty")
        itr=self.head
        lst=''
        count=0
        while itr and count<=9:
            lst+=str(itr.data)+'-->'
            itr=itr.next
            count+=1
        print(lst)
    def floydCycleDetection(self):
        fast=self.head
        slow=self.head
        slow=slow.next
        fast=fast.next.next
        while fast and fast.next  and slow!=fast :
            slow=slow.next
            fast=fast.next.next
        if slow==fast:
            print("Loop detected")
        else:
            print("No loop detected")



if __name__=='__main__':

    ll=LinkedList()
    ll.inserAt(0,2)
    ll.inserAt(1,4)
    ll.inserAt(2,7)
    ll.inserAt(3,12)
    ll.inserAt(4,14)
    ll.inserAt(5,17)
    ll.inserAt(6,149)
    ll.inserAt(7,178)
   # ll.head.next.next.next.next.next.next= ll.head.next.next.next.next
    ll.print()
    ll.floydCycleDetection()
