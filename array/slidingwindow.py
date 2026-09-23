def maxsubarray(a,k):
  sum=0;
  for i in range(k):
    sum+=a[i]
  max=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if sum>max:
      max=sum
  print(max)
a=[1,2,3,4,5,6,7,1]
print(a)
maxsubarray(a,3)