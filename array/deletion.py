def delete(ar,el):
  ar2=[0 for i in range(len(a)-1)]
  for i in range(el):
    ar2[i]=ar[i]
  for i in range(el,len(ar)-1):
    ar2[i]=a[i+1]
  return ar2  
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
el=int(input())
a=delete(a,el)
print(a)