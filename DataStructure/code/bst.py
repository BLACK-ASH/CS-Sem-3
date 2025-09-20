class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.insert(root.right,data)
        else:
            root.left = self.insert(root.left,data)
        return root

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.inorder(root.left)
        self.inorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data,end=" ")

c = BST()
c.root = c.insert(c.root,23)
c.root = c.insert(c.root,13)
c.root = c.insert(c.root,43)

print("Inorder : ",end=" ")
c.inorder(c.root)
print()

print("Pre-order : ",end=" ")
c.preorder(c.root)
print()

print("Post-order : ",end=" ")
c.postorder(c.root)
print()
