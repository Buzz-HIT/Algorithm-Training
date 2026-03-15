def isValid(s):
    stack = []
    sList = list(s)
    for i in range(len(sList)):
        if sList[i] == '(' or sList[i] == '{' or sList[i] == '[':
            stack.append(sList[i])
        else:
            if not stack:
                return False
            tmp = stack.pop()
            if sList[i] == ')' and tmp != '(':
                return False
            if sList[i] == '}' and tmp != '{':
                return False
            if sList[i] == ']' and tmp != '[':
                return False
    return True if not stack else False

s = "([)]"
print(isValid(s))