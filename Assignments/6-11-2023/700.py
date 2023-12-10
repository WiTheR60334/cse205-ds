class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            print(root.val)
            if root.val==val:
                return root
            l=dfs(root.left)
            r=dfs(root.right)
        return dfs(root)