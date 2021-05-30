def patternSearching(string,pattern):
  "This is naive method of Pattern matching"
  s=string
  p=pattern
  N=len(string)
  n=len(pattern)
  t=[]
  index=0
  for i in range(N):
    if(s[i]==p[i%n] and i%n !=0):
      t.append(s[i])

    elif("".join(t)==p):
      print(index)
      t = []
      if(s[i]==p[i%n]):
        t.append(s[i])
        index=i
    else:
      t=[]
      if (s[i] == p[i % n]):
        t.append(s[i])
        index=i


patternSearching('abacaba','aba')



patternSearching("abacabacdseabab","aba")



