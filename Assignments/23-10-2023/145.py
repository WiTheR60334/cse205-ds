class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return postorder(root)