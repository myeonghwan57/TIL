import sys 
input = sys.stdin.readline
while True:    
    str = input()
    stack = []
    if char == '.':
            break
    for char in str:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')') 
                break
        elif char == ']': 
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']') 
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')