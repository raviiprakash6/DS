def leftMostRepeatingCharacter(s1):
    """THis function will return the left most repeating character present in String
    """
    char=[0]*256
    for i in s1:
        if(char[ord(i)]>0):
            return i
        else:
            char[ord(i)]+=1
    return -1

s1="=<>a<="
print(leftMostRepeatingCharacter(s1))


