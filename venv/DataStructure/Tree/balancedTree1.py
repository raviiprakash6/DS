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


def balancedTree(node):

    if node==None:
        return True
    lh=heightOfBinaryTree(node.left)
    rh=heightOfBinaryTree(node.right)

    return abs(lh-rh)<=1 and balancedTree(node.left) and balancedTree(node.right)

root=Node(1)
root.left=Node(4)
# root.right=Node(6)
# root.right.right=Node(16)
# root.right.right.right=Node(17)
root.left.left=Node(20)
# root.left.left.left=Node(77)
print(balancedTree(root))
