# Assume: pop, top and getMin will always be called on non-empty stacks.
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val : int) -> None:
        if len(self.stack) == 0:
            min_val = val
        else:
            top_item = self.stack[len(self.stack) - 1][1]
            min_val = val if top_item > val else top_item
        self.stack.append((val, min_val))
    def pop(self) -> None:
        return self.stack.pop()[0]
    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]
    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]

ms = MinStack()
ms.push(5)
ms.push(0)
ms.push(4)
ms.push(2)
print(ms.getMin() == 0)
