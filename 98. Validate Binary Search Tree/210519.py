import math
class Solution:
    def isValidBST(self, root):
        return self.isValid(root, -math.inf, math.inf)

    def isValid(self, root, mn, mx):
        if not root:
            return True
        if root.val <= mn or mx <= root.val:
            return False
        return self.isValid(root.left, mn, root.val) and self.isValid(root.right, root.val, mx)
