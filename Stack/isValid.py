def isValid(s: str) -> bool:
    combination = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
    }
    stack = []
    for i in range(len(s)):
        if s[i] in combination:
            stack.append(s[i])
        elif len(stack) != 0:
            latestSymbol = stack[len(stack) - 1] 
            if combination[latestSymbol] != s[i]:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(isValid("([)]") == False)
print(isValid("()[]{}") == True)