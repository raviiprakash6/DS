class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def addAtBegnining(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while (itr.next):
            itr = itr.next
        itr.next = Node(data)

    # O(2n)
    def segregateEvenOddWay1(self):
        itr = self.head
        last = None
        count = 0
        prev_head = None
        prev = None
        oddhead = self.head
        while (itr):
            last = itr
            itr = itr.next
            count = count + 1
        itr = self.head
        while count > 0:
            if itr.data % 2 != 0 and prev is None:
                temp = itr
                itr = itr.next
                temp.next = None
                last.next = temp
                last = last.next
                count -= 1
            elif itr.data % 2 != 0 and prev:
                if prev_head is None:
                    prev_head = prev
                temp = itr
                itr = itr.next
                prev.next = prev.next.next
                temp.next = None
                last.next = temp
                last = last.next
                count -= 1

            else:
                if prev_head is None:
                    prev_head = prev
                prev = itr
                itr = itr.next
                count -= 1
        self.head = prev_head if prev else oddhead

    def print(self):
        itr = self.head
        if itr == None:
            print("Linked List Is Empty")
        lst = ''
        while (itr):
            lst += str(itr.data) + '-->'
            itr = itr.next
        print(lst)


if __name__ == '__main__':
    ll = LinkedList()
    ll.addAtBegnining(172)
    ll.addAtBegnining(52)
    ll.addAtBegnining(92)
    ll.addAtBegnining(12)
    ll.addAtBegnining(45)
    ll.addAtBegnining(44)
    ll.addAtBegnining(46)
    ll.print()
    ll.segregateEvenOddWay1()
    ll.print()
