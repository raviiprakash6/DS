class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None


    def addAtEnd(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node


    def print(self):
        itr=self.head
        if itr is None:
            print(List is Empty)
            return
        lst=''
        while itr:
            lst+=str(itr.data)+'-->'
            itr=itr.next
        print(lst)

    def nthNodeFromEnd(self,n):
        itr=self.head
        low=itr
        high=itr
        for i in range(0,n):
            high=high.next

        while high:
            low=low.next
            high=high.next
        return low.data




if __name__=='__main__':
    ll=LinkedList()
    ll.addAtEnd(2)
    ll.addAtEnd(5)
    ll.addAtEnd(6)
    ll.addAtEnd(7)
    ll.addAtEnd(9)
    ll.addAtEnd(1)
    ll.addAtEnd(3)
    ll.print()
    print(ll.nthNodeFromEnd(7))