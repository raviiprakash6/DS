class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None


    def addAtBegnining(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data)

#O(2n)
    def segregateEvenOddWay1(self):
        itr=self.head
        last=None
        count=-1
        while(itr):
            last=itr
            itr=itr.next
            count=count+1

















    def print(self):
        itr =self.head
        if itr ==None:
            print("Linked List Is Empty")
        lst=''
        while(itr):
            lst+=str(itr.data)+'-->'
            itr=itr.next
        print(lst)


if __name__=='__main__':
    ll=LinkedList()
    ll.addAtBegnining(7)
    ll.addAtBegnining(52)
    ll.addAtBegnining(9)
    # ll.addAtBegnining(12)
    # ll.addAtBegnining(45)
    # ll.addAtBegnining(44)
    # ll.addAtBegnining(46)
    ll.print()
    ll.segregateEvenOddWay1()
    ll.print()