# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def prune(self, root):
        if not root:
            return False
        if root.left:
            if not self.prune(root.left):
                root.left = None
        if root.right:
            if not self.prune(root.right):
                root.right = None
        return bool(root.left or root.right or root.val==1)
        
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.prune(root)
        return root

    