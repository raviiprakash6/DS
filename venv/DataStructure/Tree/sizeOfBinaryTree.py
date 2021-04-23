class Node:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
count=0
def sizeOfBinaryTree(data):
    global count
    if data.node !=None:
        count=count+1
    else:
        return 0
    if data.left:
        sizeOfBinaryTree(data.left)
    if data.right:
        sizeOfBinaryTree(data.right)
    return count



root=Node(1)
root.left=Node(4)
root.right=Node(6)
# root.right.right=Node(16)
# root.left.left=Node(8)
# root.left.left.left=Node(7)
print(sizeOfBinaryTree(root))
