
def sum(array,idx):
  if idx>= len(array):
    return 0
  return array[idx]+ sum(array,idx+1)

sum= sum([1,2,3,4,5],0)
print(sum)