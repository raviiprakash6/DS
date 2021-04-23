class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("List is empty")

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr=itr.next
        print(llstr)

    def insertAtBeginning(self,data):
        node = Node(data, self.head)
        self.head=node


    def insertAtEnd(self,data):

        if self.head is None:
            self.head=Node(data)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertAt(self,index,data):
        if(index==0):
            insertAtBegining(data)
        if(index==self.getLength()):
            insertAtEnd(data)

        count=0
        itr=self.head
        while itr:
            if(count==index-1):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count=count+1

    def removeAtBeginning(self):
         itr=self.head
         self.head=itr.next

    def removeAtEnd(self):
        itr = self.head
        while(itr.next.next):
            itr=itr.next
        itr.next=None


    def removeAt(self,index):
        itr=self.head
        count=0
        while itr:
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1




if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(5)
    ll.insertAtEnd(87)
    ll.insertAtEnd(98)
    ll.insertAt(1,80)
    ll.print()
    ll.removeAtBeginning()
    ll.print()
    ll.removeAtEnd()
    ll.print()
    ll.removeAt(2)
    ll.print()





