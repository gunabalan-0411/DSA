from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]


# Testing
tokens = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
]
for token in tokens:
    print(f"input: {token}")
    print(f"output: {Solution().evalRPN(tokens=token)}")
