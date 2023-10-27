class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximumSum = float("-inf")
        def rec(root):
            if not root:
                return 0
            l = max(rec(root.left),0)
            r = max(rec(root.right),0)
            temp = root.val + l + r
            self.maximumSum = max(self.maximumSum,temp)
            return max(l,r)+root.val
        rec(root)
        return self.maximumSum