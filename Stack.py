stack = []
#push
stack.append('A')
stack.append('R')
stack.append('I')
stack.append('F')
print(stack)
#pop
element = stack.pop()
print('pop: ',element)
print(stack)
#peak
peakElement = stack[-1]
print('Peak: ', peakElement)
print(stack)
#isEmpty
isEmpty = False


stack.pop()
stack.pop()
stack.pop()
print(type(len(stack)))
print(stack)

if(len(stack)<=0):
    isEmpty=True
print('isEmpty: ', isEmpty)