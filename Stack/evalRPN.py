from collections import deque
# Evaluate Reverse Polish Notation:
# You are given an array of strings tokens that represents
# a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
#    The operands may be integers or the results of other operations.
#    The operators include '+', '-', '*', and '/'.
#    Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in ["+", "-", "*", "/"]:
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    if tokens[i] == "+":
                        result = a + b
                    elif tokens[i] == "-":
                        result = a - b
                    elif tokens[i] == "*":
                        result = a * b
                    elif tokens[i] == "/":
                        result = int(a / b)
                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    break
        return int(tokens[0])

    def evalRPN_stack(self, tokens: list[str]) -> int:
            stack = deque()
            for token in tokens:
                if token == "+":
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                elif token == "-":
                    b = stack.pop()
                    prev = stack.pop()
                    res = prev - b
                    stack.append(res)
                elif token == "*":
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                elif token == "/":
                    b = stack.pop()
                    prev = stack.pop()
                    res = int(prev / b)
                    stack.append(res)
                else:
                    stack.append(int(token))
            return round(stack.pop())

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

if __name__ == '__main__':
    solution = Solution()
    checker(solution.evalRPN(["1","2","+","3","*","4","-"]), 5)
    checker(solution.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
    checker(solution.evalRPN(tokens=["4","13","5","/","+"]), 6)

    checker(solution.evalRPN_stack(["1","2","+","3","*","4","-"]), 5)
    checker(solution.evalRPN_stack(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
    checker(solution.evalRPN_stack(tokens=["4","13","5","/","+"]), 6)
