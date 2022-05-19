def stockSell(arr, c=1):
    buy = 0
    sell = 0
    profit = 0
    n = len(arr)
    if (c <= n - 1):

        for i in range(c, n):
            if (arr[i - 1] < arr[i] and buy == 0):
                buy = arr[i - 1]
            if ((buy != 0 and arr[i - 1] > arr[i])):
                sell = arr[i - 1]
                c = i + 1
            if (i == n - 1):
                sell = arr[i]
                c = i + 1
            if (sell != 0 and buy != 0):
                profit = sell - buy
                break;
    else:
        return 0
    return profit + stockSell(arr, c)

#-------------------------------------------------------------------------------------------------------#

def stockSell_1(arr, c=1):
    buy = 0
    sell = 0
    profit = 0
    n = len(arr)
    for i in range(1, n):
        if (arr[i] > arr[i - 1]):
            buy = arr[i - 1]
            sell = arr[i]
            profit += (sell - buy)
    return profit


arr=[1,5,3,1,2,8]
print(stockSell(arr, c=1))
print(stockSell_1(arr, c=1))
