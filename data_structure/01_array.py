
# 初始化
array:list= [1,2,3,4,5]
# 尾部添加元素
array.append(6)
# 指定索引添加元素
array.insert(1,0)


print(array)
# 根据索引删除元素并返回，默认最后一个
last=array.pop()
print(last)
print(array)
# 指定索引删除
frist =array.pop(1)
ss= array.remove(2)
print(frist,array)

array.append(6)
array.append(7)

print(array)



array:list=[1,2,3,4,5]
array.append(6)
array.insert(0,0) #在索引的前面插入一个值

array.remove(6)
frist=array.pop(0)

array[4]=6
array.index(4)

if 4 in array: print( array.index(4))



array2= array.reverse()
array1= array.sort()
print(array1,array2)