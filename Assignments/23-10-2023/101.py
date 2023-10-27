class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None or root1.val!=root2.val:
                return False
            return rec(root1.left,root2.right) and rec(root1.right, root2.left)
        return rec(root,root)