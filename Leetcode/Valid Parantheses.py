def isValid(s):
    stack = []
    for ch in s:
        if ch=='{' or ch == '[' or ch == '(':
            stack.append(ch)
        elif len(stack)>0:
            if ch == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ch == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif ch == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        else:
            return False
    if len(stack)>0:
        return False
    return True

s = "()"
check = isValid(s)
print(check)