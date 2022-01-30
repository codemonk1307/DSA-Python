

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found the Element")
            return self

        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)

        print("Not found the target entered")
        return None

class Tree:
    def __init__(self, root, name):
        self.root = root
        self.name = name

    # convinience in accessing wrapping technique
    def search(self, target):
        return self.root.search(target)



node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(12)
node.right.right = Node(1000)

# instantiate the Tree Class
myTree = Tree(node, "Sachin\'s Tree")

found = myTree.search(10000)

if not found:
    print("Not Found the element")
else:
    print(found.data)




print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.right.data)

# print(node.left.data)
# print(node.left.right.data)
# print(node.right.data)
# print(node.right.right.data)


