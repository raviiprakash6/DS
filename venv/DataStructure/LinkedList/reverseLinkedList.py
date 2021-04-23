class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None

    def addAtBeginning(self,data):
        node=Node(data)
        itr=self.head
        if itr is None:
            self.head=node
            return
        self.head=Node(data,self.head)

    def reverseLinkedList(self):
        itr=self.head
        prev=None
        curr =itr
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev





    def print(self):
        itr =self.head
        lst=''
        while itr:
            lst+=str(itr.data)+'-->'
            itr=itr.next
        print(lst)

if __name__ == '__main__':
    ll=LinkedList()
    ll.addAtBeginning(2)
    ll.addAtBeginning(45)
    ll.addAtBeginning(46)
    ll.addAtBeginning(47)
    ll.addAtBeginning(48)
    ll.print()
    ll.reverseLinkedList()

    ll.print()

