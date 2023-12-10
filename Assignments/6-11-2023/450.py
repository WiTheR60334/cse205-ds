class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root,key):
            if not root:
                return root
            if root.val>key:
                root.left=dfs(root.left,key)
            elif root.val<key:
                root.right=dfs(root.right,key)
            else:
                if not root.left: return root.right
                if not root.right: return root.left
                if root.left and root.right:
                    temp=root.right
                    while temp.left:
                        temp=temp.left
                    root.val=temp.val
                    root.right=dfs(root.right,root.val)
            return root
        return dfs(root,key)