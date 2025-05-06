class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a, b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif i == "/":
                a, b = stack.pop() , stack.pop()
                stack.append(int(b / a))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(i))
            
        return stack[0]

s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))