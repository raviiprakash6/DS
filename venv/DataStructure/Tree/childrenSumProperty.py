# Children Sum Property is a property in which the sum of values of the left child and right child should be equal
# to the value of their node if both children are present. Else if only one child is present then the value of the
# child should be equal to its node value.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def childrenSumProperty(node):

    if node.left!=None and node.right!=None:
        if node.data!=node.left.data+node.right.data:
            return False
        else:
            return childrenSumProperty(node.left) and childrenSumProperty(node.right)
    elif node.left==None and node.right!=None:
        if node.data!=node.right.data:
            return False
        else:
            return childrenSumProperty(node.left) and childrenSumProperty(node.right)
    elif node.right==None and node.left!=None:
        if node.data!=node.left.data:
            return False
        else:
            return childrenSumProperty(node.left) and childrenSumProperty(node.right)
    else:
        return True

    return childrenSumProperty(node.left) and childrenSumProperty(node.right)




root=Node(20)
root.left=Node(9)
root.right=Node(11)
root.right.right=Node(6)
root.right.left=Node(5)
root.left.left=Node(4)
root.left.right=Node(5)
print(childrenSumProperty(root))