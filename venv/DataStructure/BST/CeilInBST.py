class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def BinaryInsert(root,node):
    if root ==None:
        root=Node(node)
    elif node>root.data:
        if root.right==None:
            root.right=Node(node)
        else:
            BinaryInsert(root.right,node)
    elif node<root.data:
        if root.left==None:
            root.left=Node(node)
        else:
            BinaryInsert(root.left,node)
    return root




def CeilInBST(root,node):
    ceil_val=None
    while(root):
        if root.data==node:
            return root.data
        if node>root.data:
            root=root.right
        elif node<root.data:
            ceil_val=root.data
            root=root.left
    return ceil_val



if __name__ == '__main__':
    root=None
    root = BinaryInsert(root, 50)
    root = BinaryInsert(root, 30)
    root = BinaryInsert(root, 20)
    root = BinaryInsert(root, 25)
    root = BinaryInsert(root, 40)
    root = BinaryInsert(root, 70)
    root = BinaryInsert(root, 60)
    root = BinaryInsert(root, 80)
    print("The tree before the deletion:")

    key = 55

    print(CeilInBST(root,key))
