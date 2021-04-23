class Node:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None


def maxInBinaryTree(data):
    if data==None:
        return float('-inf')
    else:

        return max(data.node,max(maxInBinaryTree(data.left),maxInBinaryTree(data.right)))




print(maxInBinaryTree(root))
