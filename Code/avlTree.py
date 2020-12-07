import sys
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Height of leaf is 1

class AVLTree(object):
    def insert_node(self, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
    
    
    def getHeight(self, root):
    """Get the height of the node"""
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
    """Get balance factor of the node"""

    def _insert(value, root):

