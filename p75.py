sentence = list(str(input()))
stack=[]
for i in sentence:
    if i=='=':
        if len(stack)!=0:
            stack.pop()
    else:
        stack.append(i)

print("".join(stack))