def balancedParenthesisStack(arr):
    stac=[]
    for i in arr:
        if i in ('{','[','('):
            stac.append(i)
        elif i=='}':
            if '{'==stac.pop():
                pass
            else:
                return "unbalanced parenthesis"
        elif i==']':
            if '['==stac.pop():
                pass
            else:
                return "unbalanced parenthesis"
        elif i==')':
            if '('==stac.pop():
                pass
            else:
                return "unbalanced parenthesis"
    if len(stac) ==0:
         return "Balanced parenthesis"
    else:
         return "Unbalanced parenthesis"

arr=['{','[','}']
print(balancedParenthesisStack(arr))