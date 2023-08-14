class Solution:
    def revStr(self, i, n, s):
        if i >= n // 2:
            return
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        self.revStr(i + 1, n, s)

    def reverseString(self, s):
        n = len(s)
        self.revStr(0, n, s)


