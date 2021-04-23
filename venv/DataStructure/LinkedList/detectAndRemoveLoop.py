class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBeginning(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        itr=self.head
        self.head=Node(data,itr)


    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        itr =self.head
        lst=''
        count=0
        while itr and count <=10:
            lst+=str(itr.data)+'-->'
            itr=itr.next
            count+=1
        print(lst)

    def detectAndRemoveLoop(self):
        slow=self.head.next
        fast=self.head.next.next
        while fast.next and slow!=fast:
            slow=slow.next
            fast=fast.next.next

        if(slow==fast):
            print("loop detected")
            slow=self.head
            while(slow.next!=fast.next):
                slow=slow.next
                fast=fast.next
            fast.next=None
            print("Loop removed")
        else:
            print("No loop detected")


if __name__=='__main__':
    ll=LinkedList()
    ll.insertAtBeginning(1)
    ll.insertAtBeginning(11)
    ll.insertAtBeginning(111)
    ll.insertAtBeginning(1111)
    ll.insertAtBeginning(11111)
    ll.print()
    ll.head.next.next.next.next.next=ll.head.next.next
    ll.print()
    ll.detectAndRemoveLoop()
    ll.print()