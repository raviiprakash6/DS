class Node:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    arr = [root]
    while len(arr) > 0:
        root = arr.pop(0)
        print(root.node, end=" ")
        if root.left:
            arr.append(root.left)
        if root.right:
            arr.append(root.right)


root = Node(1)
root.left = Node(4)
root.right = Node(2)
root.right.right = Node(16)
root.left.left = Node(8)
root.left.left.left = Node(7)

levelOrderTraversal(root)
