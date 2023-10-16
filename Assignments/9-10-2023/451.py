class Solution:
    def frequencySort(self, s: str) -> str:
        temp,cnt = {},0
        for i in s:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
            cnt = max(cnt, temp[i])

        ans = []
        while cnt > 0:
            for i, freq in temp.items():
                if freq == cnt:
                    ans.append(i * freq)
                    temp[i] = 0  
            cnt -= 1

        return "".join(ans)