class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def BinaryInsert(root,node):
    if root==None:
        return Node(node)

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

def FloorInBST(root,node):
    floor_val=float('-inf')

    while root:
        if root.data<node:
            floor_val=max(floor_val,root.data)

        if root.data==node:
            return node
        elif node>root.data:
            root=root.right
        elif node<root.data:
            root=root.left
    return floor_val if floor_val > float('-inf') else None


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

    key = 69.99999

    print(FloorInBST(root,key))



###########################WIthout max condition################
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def BinaryInsert(root,node):
    if root==None:
        return Node(node)

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

def FloorInBST(root,node):
    floor_val=float('-inf')

    while root:
        # if root.data<node:
        #     floor_val=max(floor_val,root.data)

        if root.data==node:
            return node
        elif node>root.data:
            floor_val=root.data
            root=root.right
        elif node<root.data:
            root=root.left
    # return floor_val if floor_val > float('-inf') else None
    return floor_val


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

    key = 25

    print(FloorInBST(root,key))





