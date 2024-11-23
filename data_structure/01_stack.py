stack = []

stack.append(90)
stack.append(1)
stack.append(2)
stack.append(3)
item3=stack.pop()
item2=stack.pop()
item1=stack.pop()

length= len(stack)
if length>0: print(stack[length-1])

# 查看栈头
print(stack[-1])