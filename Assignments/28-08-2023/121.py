class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        temp=prices[0]
        ans=0
        for i in range(1,n):
            if temp>prices[i]:
                temp=prices[i]
            if ans<(prices[i]-temp):
                ans=prices[i]-temp  
        return ans           