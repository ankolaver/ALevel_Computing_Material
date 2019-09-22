def linears(arr,target):
  for k in arr:
    if k == target:
      return k
  return -1

#main
li = [5,2,9,10,11]
print(linears(li,9))
