class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min=float('-inf'),max=float('inf')):
            if not root:
                return True
            if not (min<root.val<max):
                return False
            return dfs(root.left,min,root.val) and dfs(root.right,root.val,max)
        return dfs(root)