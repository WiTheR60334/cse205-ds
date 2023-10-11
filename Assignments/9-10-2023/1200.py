class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        def sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left, right = arr[:mid], arr[mid:]
            left, right = sort(left), sort(right)
            ans, i, j = [], 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1

            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans
        b=sort(arr)
        diff=b[1]-b[0]
        for i in range(len(b)-1):
            if b[i+1]-b[i]<diff:
                diff=b[i+1]-b[i]
        for i in range(len(b)-1):
            if b[i+1]-b[i]==diff:
                ans.append(b[i:i+2])
        return ans
