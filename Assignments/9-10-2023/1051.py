class Solution:
    def heightChecker(self, heights: List[int]) -> int:
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
        temp=sort(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=temp[i]:
                count+=1
        return count     