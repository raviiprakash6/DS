class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def BinaryInsert(root,node):
    if root is None:
        return Node(node)
    elif root.data <node:
        if(root.right==None):
            root.right=Node(node)
        else:
            BinaryInsert(root.right,node)
    else:
        if(root.left==None):
            root.left=Node(node)
        else:
            BinaryInsert(root.left,node)
    return root
def Max_Node(root):
    root=root.left
    while (root.right):
        root=root.right
    return root

    # if root.right==None:
    #     return root
    # else:
    #     return Max_Node(root.right)

def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end = " ")
    inorder(temp.right)

def DeleteNode(root,node):
    if root is None:
        return

    if node>root.data:
        root.right=DeleteNode(root.right,node)
    elif(node<root.data):
        root.left=DeleteNode(root.left,node)
    else:

        if root.right==None:
            temp=root.left
            root=None
            return temp
        elif root.left==None:
            temp=root.right
            root=None
            return temp
        else:
            temp=Max_Node(root)
            root.data=temp.data
            root.left=DeleteNode(root.left,temp.data)
    return root

if __name__ == '__main__':
    root=None
    root = BinaryInsert(root, 50)
    root = BinaryInsert(root, 30)
    root = BinaryInsert(root, 20)
    # root = BinaryInsert(root, 25)
    root = BinaryInsert(root, 40)
    root = BinaryInsert(root, 70)
    root = BinaryInsert(root, 60)
    root = BinaryInsert(root, 80)
    print("The tree before the deletion:")
    inorder(root)
    key = 3

    root = DeleteNode(root,key)
    print()
    print("To delete",key)
    print("The tree after the deletion;")
    inorder(root)








