
class Node:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None

maxlevel=0
def printLeftView(data,level=1):
    global maxlevel
    if data==None:
        return
    if maxlevel<level:
        print(data.node)
        maxlevel=level

    if data.left:
        return printLeftView(data.left,level+1)
    if data.right:
        return printLeftView(data.right.left,level+1)


root=Node(1)
root.left=Node(4)
root.right=Node(6)
root.right.left=Node(10)
root.right.right=Node(12)
root.right.right.left=Node(18)
printLeftView(root)

#
# ___________________________________________________________________________________________
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def leftView(root):
#     if root:
#         print(str(root.data))
#     if root.left:
#         leftView(root.left)
#     if root.right:
#         if root.right.left:
#             leftView(root.right.left)
#
#
# if __name__ == "__main__":
# # tree = Node(1)
# tree.left =Node(2)
# tree.right =Node(3)
# tree.left.left =Node(4)
# tree.left.right =Node(5)
# tree.right.left =Node(6)
# tree.right.right =Node(7)

