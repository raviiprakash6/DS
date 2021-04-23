class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def printLevel(data):
    queue = []
    queue.append(data)
    while len(queue) != 0:
        data=queue.pop(0)
        print(data.data)
        if data.left:
            queue.append(data.left)
        if data.right:
            queue.append(data.right)



root=Node(1)
root.left=Node(4)
root.right=Node(6)
root.right.right=Node(16)
root.left.left=Node(8)
root.left.left.left=Node(7)
printLevel(root)