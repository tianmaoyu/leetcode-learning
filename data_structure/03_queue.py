
queue:list  = []

# 进入队列，添加队尾
queue.append(0)
queue.append(1)
queue.append(2)
# 出队列，队首 --
item0= queue.pop(0)
item1= queue.pop(0)
item2= queue.pop(0)

print(len(queue))
print(queue[0])
