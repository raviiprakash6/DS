def leftMostRepeatingCharacter(str):
    """THis function will return the index of left most repeating character present in String
    """
    char=[-1]*256
    min_index= float('inf')
    for i in range(0,len(str)):
        if char[ord(str[i])] == -1:
            char[ord(str[i])]=i
        else:
            min_index=min(min_index,char[ord(str[i])])

    if min_index == float('inf'):
        return -1
    return min_index


s1="=<>a"
print(leftMostRepeatingCharacter(s1))


