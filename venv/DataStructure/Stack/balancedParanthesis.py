def balancedParenthesis(arr):
    n=len(arr)-1
    i=1
    for i in range(i,n):
        while(i<n and ((arr[i]=='[' and arr[i+1]==']') or (arr[i]=='(' and arr[i+1]==')') or (arr[i]=='{' and arr[i+1]=='}'))):
            del(arr[i])
            del(arr[i])
            i=i-1
            n=len(arr)-1
    if(n<0):
        print("balanced parenthesis")
    else:
        print("Non balanced parenthesis")



arr=['[','(','{']
balancedParenthesis(arr)


