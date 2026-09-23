def rotaion(a,key):
  ar=[0 for i in range(len(a))]
  ind=0
  for i in range(len(a)-key,len(a)):
    ar[ind]=a[i]
    ind+=1
  for i in range(len(a)-key):
    ar[ind]=a[i]
    ind+=1  
  return ar 
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
ind=int(input())
a=rotaion(a,ind)
print(a)