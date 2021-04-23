class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.data =data

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insertAtBeginning(self,data):

        itr=self.head
        if itr:
            self.head=Node(data,None,itr)
            itr.prev=self.head
        else:
            self.head=Node(data)

    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
        new_node.prev=itr
    def getLength(self):
        count=0
        a=0
        itr =self.head
        while itr != None:
            count+=1
            itr=itr.next
        return count

    def insertAt(self,data,index):


        if index==0:
            self.insertAtBegning(data)
            return
        if (index==self.getLength()):
            self.insertAtEnd(data)
            return
        count=0
        itr=self.head


        new_node = Node(data)
        while itr:
            if(count==index-1):
                new_node.next=itr.next
                itr.next=new_node
                new_node.prev=itr
                new_node.next.prev=new_node
                break
            itr.next
            count+=1


    def dropAtBeginning(self):
        itr=self.head
        self.head=itr.next
        itr.next = None
        self.head.prev=None

    def dropAtEnd(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.prev.next=None

    def dropAt(self,index):
        if(index==0):
            dropAtBeginning()
            return
        if(index==self.getLength()):
            dropAtEnd()
            return

        itr=self.head
        count=0
        while(itr):
            if(count==index-1):
                itr.next=itr.next.next
                itr.next.prev=itr

            itr=itr.next
            count+=1








    def print(self):
        if self.head is None:
            print("Linked List is Empty")

        itr=self.head
        lstr=''
        while itr:
            lstr+= str(itr.data) + '<==>'
            itr=itr.next
        print(lstr)


if __name__=='__main__':
    dl=DoublyLinkedList()
    dl.insertAtBeginning(23)
    #dl.insertAtBeginning(2)
    # dl.insertAtEnd(54)
    # dl.insertAtBeginning(27)
    # dl.insertAtBeginning(28)
    # dl.insertAt(47,1)
    # dl.insertAtEnd(58)
    # dl.print()
    # dl.dropAtBeginning()
    # dl.print()
    # dl.dropAtEnd()
    # dl.print()
    # dl.dropAt(2)
    dl.print()

