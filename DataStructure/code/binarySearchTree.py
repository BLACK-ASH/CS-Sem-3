class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data,root=None):
        if root is None:
            if self.root is None:
                self.root = Node(data)
                return self.root
            return Node(data)
        
        if root.data < data:
            root.right = self.insert(data,root.right)
        else:
            root.left = self.insert(data,root.left)

        return root

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" " )
        self.inorder(root.right)
