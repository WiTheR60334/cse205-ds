class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder([x for x in preorder if x < preorder[0]])
        node.right = self.bstFromPreorder([x for x in preorder if x > preorder[0]])
        return node