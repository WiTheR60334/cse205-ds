class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
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
        prices=sort(prices)
        return money-prices[0]-prices[1] if prices[0]+prices[1]<=money else money