class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            l,r=dfs(root.left),dfs(root.right)
            if l<0 or r<0 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        return dfs(root)>=0