def patternSearching(str, p1):
  "This is naive method of Pattern matching O((n1-n2+1)*n2)"
  n1 = len(str)
  n2 = len(p1)
  for i in range(0, n1 - n2 + 1):
    for j in range(0, n2):
      if str[i + j] != p1[j]:
        break
    if j == n2 - 1:
      print(i)


#####################################

def patternSearching(string,pattern):
  "This is naive method of Pattern matching which only check if pattern is present or not"
  s=string
  p=pattern
  N=len(string)
  n=len(pattern)
  t=[]
  index=0
  for i in range(N):
    if(s[i]==p[i%n]):
      t.append(s[i])
    elif("".join(t)==p):
      print(index)
      t=[]
    else:
      t=[]
      index=i+1
  return (index if("".join(t)==p) else False)

print(patternSearching('abacaba','aba'))







