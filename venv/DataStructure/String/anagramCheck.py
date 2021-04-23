def anagramCheck(s1,s2):
    char=[0]*256
    if(len(s1)!=len(s2)):
        return False
    for i in s1:
        char[ord(i)]=char[ord(i)]+1
    for i in s2:
        char[ord(i)]=char[ord(i)]-1
        
    for i in char:
        if i!=0:
            return False

    return True


s1="aba"
s2="aab"
print(anagramCheck(s1,s2))
