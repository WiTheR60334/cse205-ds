class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        d=defaultdict(list)
        queue.append([root,0,0])
        while queue:
            node,c,r=queue.popleft()
            d[c].append([r,node.val])
            if node.left:
                queue.append([node.left,c-1,r+1])
            if node.right:
                queue.append([node.right,c+1,r+1])
        ans=[]
        for i in sorted(d):
            temp=d[i]
            temp.sort()
            t=[]
            for j in temp:
                t.append(j[1])
            ans.append(t)
        return ans