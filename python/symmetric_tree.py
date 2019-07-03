"""Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        # If enpty, tree is symmetric
        if root == None:
            return True
        # Check that values of root's children are equal            
        return self.isMirror(root.left, root.right)

    def isMirror(self, a, b):
        if a == None and b == None:
            return True
        # If either side is None, or values aren't equal then tree is not symmetric
        elif a == None or b == None or a.val != b.val:
            return False 
        
        else:
            # Checkout that the outer and inner pieces of tree are equal
            return self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)