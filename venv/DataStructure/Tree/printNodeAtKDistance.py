class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def printNodeAtKDistance(node,k):
    if node == None:
        return
    if k==0:
        print(node.data)
    else:
        printNodeAtKDistance(node.left,k-1)
        printNodeAtKDistance(node.right,k-1)





root=Node(1)
root.left=Node(4)
root.right=Node(6)
root.right.right=Node(16)
root.left.left=Node(8)
root.left.left.left=Node(7)
printNodeAtKDistance(root,2)