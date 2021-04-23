def leftMostNonRepeatingCharater(s1):
    char=[-1]*256
    n=len(s1)
    res=-1
    for i in range(n):
        if(char[ord(s1[i])]==-1):
            char[ord(s1[i])]=i
        else:
            char[ord(s1[i])] = -2
    n1=len(char)
    for i in range(1,n1):
        if(char[i]>-1 and res==-1 ):
            res=char[i]
        elif(char[i]>-1):
            res = min (res,char[i])
    if(res>-1):
        return s1[res]
    else:
        return -1


s1="strstrefge"
print(leftMostNonRepeatingCharater(s1))




