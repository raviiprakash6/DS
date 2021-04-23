class Node:
    def __init__(self,data1=None,next=None):
        self.data1=data1
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def addAtBeginnig(self,data1):
        node=Node(data1,self.head)
        self.head=node


    def print(self):
        itr=self.head
        if self.head is None:
            print("List is Empty")
            return
        lst=''
        while itr:
            lst+=str(itr.data1)+'-->'
            itr=itr.next
        print('Linked list is '+lst)
    def middleElement(self):
        if self.head is None:
            return "Linked List is empty"
            return
        itr=self.head
        fast=slow=itr
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return 'Middle element is '+ str(slow.data1)






if __name__=='__main__':
    ll=LinkedList()
    ll.addAtBeginnig(2)
    ll.addAtBeginnig(22)
    ll.addAtBeginnig(25)
    ll.addAtBeginnig(29)
    ll.addAtBeginnig(21)
   # ll.addAtBeginnig(23)
    ll.print()
    print(ll.middleElement())