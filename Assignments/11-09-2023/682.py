class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="+":
                a=stack[-2]+stack[-1]
                stack.append(a)
            else:
                stack.append(int(i))
        return sum(stack)