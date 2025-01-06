class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def insert(self, data):
        new_bst = BSTNode(data)
        prev = None
        # init first root node
        if self.root == None:
            self.set_root(data)
            return 0

        # Locate null subtree for insertion
        if new_bst.data < self.get_root():
            while self.get_root().left != None:
                prev = self.get_root()
                self.set_root(prev)
            self.set_root(new_bst)
            return 0
        else:
            while self.get_root().right != None:
                prev = self.get_root()
                self.set_root(prev)
            self.set_root(new_bst)
            return 0

    def preorder(self):
        current = self.root
        