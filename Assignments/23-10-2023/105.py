class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def rec(preorder, inorder):
            if not preorder or not inorder:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)

            root.left = rec(preorder, inorder[:root_index])
            root.right = rec(preorder, inorder[root_index + 1:])

            return root
        return rec(preorder,inorder)