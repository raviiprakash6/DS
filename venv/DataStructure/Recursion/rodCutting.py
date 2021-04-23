#Number of chidern is equal to number of recursive call here we have 3 children so 3 recursive call
def rodCutting(rodLength,cut1,cut2,cut3):
    if rodLength==0:
        return 0
    elif rodLength<=-1:
        return -1

    res= max(rodCutting(rodLength-cut1,cut1,cut2,cut3),rodCutting(rodLength-cut2,cut1,cut2,cut3),rodCutting(rodLength-cut3,cut1,cut2,cut3))
    if res >=0:
        return res+1
    else:
        return -1

print(rodCutting(19,15,4,10))