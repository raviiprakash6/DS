def patternSearching(string,pattern):
  "This is naive method of Pattern matching"
  s=string
  p=pattern
  N=len(string)
  n=len(pattern)
  t=[]
  for i in range(N):
    if(s[i]==p[i%n]):
      t.append(s[i])
    elif("".join(t)==p):
      return True
    else:
      t=[]
  return (True if("".join(t)==p) else False)

print(patternSearching('abcaba','aba'))







