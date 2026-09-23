def remove_duplicates(arr):
  ind=1
  ar=[1]
  for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
      ar.append(arr[i])
      ind+=1
  return ar
n=[1,2,2,2,3,3,3,4,5]
res=remove_duplicates(n)
print(res)