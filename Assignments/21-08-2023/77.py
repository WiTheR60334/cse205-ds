class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def rec(start, curr):
            if len(curr) == k:
                return ans.append(curr.copy())
            for i in range(start, n+1):
                curr.append(i)
                rec(i + 1, curr)
                curr.pop()
        ans = []
        rec(1, [])
        return ans