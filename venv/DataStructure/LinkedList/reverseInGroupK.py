class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data)


    def reverseInGroup(self,k):
        first=None
        curr=self.head
        while curr:
            itr=curr
            prev=None
            count=1
            while curr and count<=k:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
                count+=1
            if first== None and curr:
                self.head=prev
                first=itr
                prev=itr
            elif(first==None and curr==None):
                self.head=prev
            else:
                first.next=prev
                first=itr


    def print(self):
        itr =self.head
        lst=''
        while itr:
            lst+=str(itr.data)+'-->'
            itr=itr.next
        print(lst)

if __name__ == '__main__':
    ll=LinkedList()
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.insertAtEnd(5)
    ll.insertAtEnd(7)
    ll.insertAtEnd(8)
    ll.insertAtEnd(9)
    ll.insertAtEnd(17)
    ll.insertAtEnd(18)

    ll.insertAtEnd(19)
    ll.print()
    ll.reverseInGroup(3)
    ll.print()