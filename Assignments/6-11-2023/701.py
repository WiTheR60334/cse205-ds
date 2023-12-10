class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return TreeNode(val)
            if root.val>val:
                root.left=dfs(root.left)
            else:
                root.right=dfs(root.right)
            return root
        return dfs(root)