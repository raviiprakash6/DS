def stringRotation(str1,str2):
    """This function check if the str2 can be get after rotationg str1"""
    N=len(str1)
    n=len(str2)
    j=0
    if(n!=N):
        return False
    while(str1[0]!=str2[j] and j<N):
        j+=1
    for i in range(N):
        if(str1[i]!=str2[(j+i)%N]):
            return False

    return True



print(stringRotation('abaaa','baaaa'))
