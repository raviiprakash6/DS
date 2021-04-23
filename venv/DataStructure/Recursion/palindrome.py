def palindrome(str,n,k=0):
    if str[k]!=str[n-1]:
        return False
    elif n==1 or n<=k:
        return True


    return palindrome(str,n-1,k+1)

print(palindrome('lsasl',5))

#Time complexity =BigO(n)
#Auxiliary space=BigO(n/2)i.e O(n)