def countOfChar(str):
    """This function will print the count of occurence of character"""
    count=[0]*26
    for i in str:
        count[ord(i)-97]+=1

    for i in range(len(count)):
        if(count[i]>0):
            print(chr(97+i),count[i])


str="geekforgeek"
print(countOfChar(str))


