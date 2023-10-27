class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def diameter(root):
            if not root:
                return 0
            l,r=diameter(root.left),diameter(root.right)
            self.d = max(self.d, l+r)
            return 1+max(l,r)
        diameter(root)
        return self.d