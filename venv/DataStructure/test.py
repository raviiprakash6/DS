class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def childrenSumProperty(root):
    if root.left and root.right:
        if root.data!=root.left.data+root.right.data:
            return "NO"
        else:
            childrenSumProperty(root.left)
            childrenSumProperty(root.right)
    elif root.left:
        if root.data!=root.left.data:
            return "NO"
        else:
            childrenSumProperty(root.left)
    elif root.right:
        if root.data!=root.right.data:
            return "NO"
        else:
            childrenSumProperty(root.right)




root=Node(20)
root.left=Node(9)
root.right=Node(11)
root.right.right=Node(6)
root.right.left=Node(5)
root.left.left=Node(4)
root.left.right=Node(15)
print(childrenSumProperty(root))

