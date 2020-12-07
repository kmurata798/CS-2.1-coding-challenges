import sys
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 # Height of leaf is 1

class AVLTree(object):
    def insert_node(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        # if balance factor is greater than 1, then need to rotate
        if balanceFactor > 1:
            if value < root.left.value:
                returnself.rightRotate(root)
            else:
                # Need to rotate twice to balance tree
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        # if balance factor is less than -1
        if balanceFactor < -1:
            if value < root.right.value:
                return self.leftRotate(root)
            else:
                # rotate twice to balance tree
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
    
    def getHeight(self, root):
        """Get the height of the node"""
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        """Get balance factor of the node"""
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def leftRotate(self, z):
        """z is the root node"""
        # Setting current tree
        y = z.right
        T2 = y.left

        # Swapping root(z) with right(y)
        y.left = z
        z.right = T2

        # Updating node heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return new root node
        return y
    
    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # 
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return new root node
        return y

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)