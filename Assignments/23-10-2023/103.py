class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        ans,tp=[],True
        while queue:
            l=len(queue)
            temp=[]
            for _ in range(l):
                if tp:
                    node=queue.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node=queue.pop()
                    temp.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            ans.append(temp)
            tp=not tp
        return ans