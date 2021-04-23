#Number of chidern is equal to number of recursive call here we have 2 children so 2 recursive call
def subSetOfString(string,str=" ",index=0):
    length=len(string)
    if index==length:
        print(str)
        return
    subSetOfString(string, str, index+1)
    subSetOfString(string,str+(string[index]),index+1)


subSetOfString('avc')
