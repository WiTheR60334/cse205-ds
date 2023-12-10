class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans[k-1]