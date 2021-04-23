def countOfFrequencyOfArrrayElement(arr):
    dic=dict()
    n=len(arr)
    for i in range(n):
        if arr[i] in dic.keys():
            dic[arr[i]]+=1
        else:
            dic[arr[i]]=1

    return [print(key,value) for (key,value) in dic.items()]
    # Y =[x for x in sorted(dic.values(), reverse=True)]
    # second_largest= Y[1]
    # for (key,value) in dic.items():
    #     if value==second_largest:
    #         print(key)





arr=['a','b','c','d','c','c','d','f']
countOfFrequencyOfArrrayElement(arr)

