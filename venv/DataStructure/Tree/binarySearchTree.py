class BinaryNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,value):
         if self.data==value:
             return
         elif(value<self.data):
             if self.left:
                 self.left.add_child(value)
             else:
                 self.left=BinaryNode(value)
         else:
             #add data to right subtree
             if self.right:
                 self.right.add_child(value)
             else:
                 self.right=BinaryNode(value)
    def inOrder_traversal(self):
        #L->Root->R
        arr=[]
        #left element
        if self.left:
            arr+=self.left.inOrder_traversal()
        #Root
        arr.append(self.data)
        #Right element
        if self.right:
            arr+=self.right.inOrder_traversal()
        return arr

    def search(self,val):
        if self.data == val:
            return "Element found"
        elif val < self.data:
            if self.left:
                 return self.left.search(val)
            else:
                return "Element not found"
        else:
            if self.right:
                return self.right.search(val)
            else:
                return "Element not found"







def buildTree(elem):
    #assign first element as root node
    root=BinaryNode(elem[0])
    for i in range (1,len(elem)):
     root.add_child(elem[i])
    return root

if __name__=='__main__':
    number=[12,2,1,5,8,1,3]
    tree=buildTree(number)
    #print(tree.inOrder_traversal())
    print(tree.search(15))

