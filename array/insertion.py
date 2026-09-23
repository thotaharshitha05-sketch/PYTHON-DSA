def insert(ar,el,ind):
  ar2=[0 for i in range(len(a)+1)]
  for i in range(ind):
    ar2[i]=ar[i]
  for i in range(ind,len(ar)):
    ar2[i+1]=a[i]
  ar2[ind]=el
  return ar2  
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
el=int(input())
ind=int(input())
a=insert(a,el,ind)
print(a)