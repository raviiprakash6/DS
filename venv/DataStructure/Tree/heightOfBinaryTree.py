class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def heightOfBinaryTree(node):
    if node==None:
        return 0
    else:
        return max(heightOfBinaryTree(node.left),heightOfBinaryTree(node.right))+1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.left.left = Node(6)
root.left.left.left.left.left = Node(7)
print(heightOfBinaryTree(root))


