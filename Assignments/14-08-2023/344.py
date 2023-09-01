class Solution:
    def reverseString(self, s):
        end = len(s) - 1
        def recursiveReverse(s, i):
            if i < len(s)/2:
                s[i], s[end-i] = s[end-i],s[i]
                i =  i + 1
                recursiveReverse(s,i)
            else:
                return
        recursiveReverse(s,0)
