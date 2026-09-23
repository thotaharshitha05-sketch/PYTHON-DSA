def rotation(a,key):
  ar=[0 for i in range(len(a))]
  ind=0
  for i in range(key,len(a)):
    ar[ind]=a[i]
    ind+=1
  for i in range(key):
    ar[ind]=a[i]
    ind+=1
  return ar
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
ind=int(input())
a=rotation(a,ind)
print(a)