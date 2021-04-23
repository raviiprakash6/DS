class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head1=None
        self.head2=None

    def print(self):
        itr=self.head1
        itr1=self.head2
        lst=''
        while(itr):
            lst+=str(itr.data)+'--:>'
            itr=itr.next
        print(lst)
        lst=''
        while(itr1):
            lst+=str(itr1.data)+'--:>'
            itr1=itr1.next
        print(lst)

    def intersectionOfTwoLinkedList(self):
        itr1=self.head1
        itr2=self.head2
        count1=0
        count2=0
        if(itr1==None or itr2==None):
            return print("One Linked list is empty")

        while itr1:
            itr1=itr1.next
            count1+=1
        while itr2:
            itr2=itr2.next
            count2+=1
        n=abs(count1-count2)
        c1=0
        itr1=self.head1
        itr2=self.head2
        if(itr1==itr2):
            return itr1.data

        if(count1>=count2):
            while(c1<n):
                itr1=itr1.next
                c1+=1
            while(itr1!=itr2):

                if(itr1.next==None or itr2.next==None):
                    return print("No intersection found")
                elif(itr1.next==itr2.next):
                    return print(str(itr1.next.data))

                else:
                    itr1=itr1.next
                    itr2=itr2.next

        if (count2 >= count1):
            while (c1 < n):
                itr2 = itr2.next
                c1 += 1
            while (itr1 != itr2):

                if (itr1.next == None or itr2.next == None):
                    return print("No intersection found")
                elif (itr1.next == itr2.next):
                    return print(str(itr1.next.data))
                else:
                    itr1 = itr1.next
                    itr2 = itr2.next

        


if __name__=='__main__':


    ll=LinkedList()
    ll.head1=Node(3)
    ll.head1.next=Node(7)
    ll.head1.next.next=Node(8)
    ll.head1.next.next.next = Node(10)
    # ll.head2=Node(4)
    # ll.head2.next=Node(6)
    # ll.head2.next.next=ll.head1.next
    ll.print()
    ll.intersectionOfTwoLinkedList()


