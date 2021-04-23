class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)


    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")


    def preorder(self,start,traversal):
        #Root->Left->Right
        if start:
            traversal+=str(start.data)+"-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    def inorder(self,start,traversal):
        #Left->Root->Right
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=(str(start.data)+"-")
            traversal=self.inorder(start.right,traversal)
        return traversal

    def postorder(self,start,traversal):
        #Left->Right->Root
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal += str(start.data) + "-"
        return traversal
if __name__=="__main__":
    tree = BinaryTree(1)
    tree.root.left =Node(2)
    tree.root.right =Node(3)
    tree.root.left.left =Node(4)
    tree.root.left.right =Node(5)
    tree.root.right.left =Node(6)
    tree.root.right.right =Node(7)
    print("Pre order traversal",tree.print_tree("preorder"))
    print("In order traversal",tree.print_tree("inorder"))
    print("Post order traversal",tree.print_tree("postorder"))

