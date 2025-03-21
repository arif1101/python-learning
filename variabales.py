number = 3
strToNmbr= str(number)
print('number : ', number,type(number))
print('string : ',strToNmbr,type(strToNmbr))

name1,name2,name3 = 'arif','zakia','munni'
print(name1, name2, name3)

# multiple value assinged in same variables
print('---multiple value assinged in same variables---')
person1=person2=person3='arif'
print(person1,person2,person3)

# unpack collection
print('---unpack collection---')
fruits = ['apple','banana', 'cherry']
x,y,z=fruits
print(x)
print(y)
print(z)

# global variables 
print('---global variables---')
globalInt = 2024
globalStr = 'arif'
def privateFnc():
    print('this is from global : ', globalInt, globalStr)

def globalChange():
    global globalStr
    globalStr = 'zakia'
    print('here our changed global value : ', globalInt, globalStr)

privateFnc()
globalChange()