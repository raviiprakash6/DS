
class BinaryHeap:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size=0
        self.Heap=[0]*(self.maxsize+1)


    def parent(self,pos):
        return (pos-1)//2

    def left(self, pos):
        return 2 * pos + 1

    def right(self, pos):
        return 2 * pos + 2

    def swap(self, pos1, pos2):
        self.Heap[pos1],self.Heap[pos2]= self.Heap[pos2],self.Heap[pos1]

    def isLeaf(self,pos):
        if pos>= self.size//2  & pos<self.size:
            return True
        return False


    def insert(self,data):
        self.heap[]



        











