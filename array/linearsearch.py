def linearsearch(a,ele):
  ar=[]
  for i in range(len(a)):
    if a[i]==ele:
      ar.append(i)
  return ar    
a=[12,33,2,4,11,10,33,33]
ele=33
print(linearsearch(a,ele))