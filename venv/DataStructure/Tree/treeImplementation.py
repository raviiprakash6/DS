class Node:
    def __init__(self,data):
        self.data=data
        self.childern=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.childern.append(child)

    def getLevel(self):
        level=0
        p=self.parent
        while(p):
            level+=1
            p=p.parent
        return level


    def print_tree(self):
        spaces=' ' * self.getLevel() * 3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree()

def build_tree():
    root=Node("Electornics")
    laptop = Node("Laptop")
    phone = Node("phone")
    tv = Node("TV")
    root.add_child(laptop)
    laptop.add_child(Node("Mac"))
    laptop.add_child(Node("Linux"))
    laptop.add_child(Node("Window"))

    root.add_child(phone)
    phone.add_child(Node("Andriod"))
    phone.add_child(Node("Window"))
    phone.add_child(Node("Mac"))

    root.add_child(tv)
    tv.add_child(Node("Smart TV"))
    tv.add_child(Node("LCD"))
    tv.add_child(Node("LED"))


    root.print_tree()

if __name__=='__main__':
    build_tree()

