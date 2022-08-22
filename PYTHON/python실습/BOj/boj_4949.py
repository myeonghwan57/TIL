import sys
input = sys.stdin.readline
 
while True:
    s = input().rstrip()
    if s == '.':    # 종료 조건
        break
 
    stack = []
    flag = True    # 짝을 이루지 않는 경우
 
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
 
        elif stack and (s[i] == ')' or s[i] == ']'):  # stack은 있지만 닫힌 괄호가 나오는 경우
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:    # (])
                flag = False
 
        elif not stack and (s[i] == ')' or s[i] == ']'):  # stack이 없으면서 닫힌 괄호가 나오는 경우, )(
            flag = False
 
    if flag and not stack:
        print('yes')
    else:
        print('no')