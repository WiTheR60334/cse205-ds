class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = {}
        def finder(node):
            if not node:
                return False
            if node.val in ans:
                return True
            ans[k - node.val] = True
            return finder(node.left) or finder(node.right)
        return finder(root)