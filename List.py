fruits = ["banana", "apple", "orange", "cherry", "mango"]
name = ["dilruba", "munni", "rakib", "arif", "zakiya"]
numbers = ["6", "8", "3", "4", "5","1"]
print("type of array : ", type(fruits))
print("length of fruits list : ", len(fruits))
constructorList = list(("tuple", "list", "dictonary", "set"))
print("constructorList : ", type(constructorList))
######### Access list ########
print("-----------list access----------")
print(fruits)
print("fruits[1] : ", fruits[1])
print("fruits[-2] : ", fruits[-2])
fruits[1] = "angur"
print("change fruits value : ", fruits)
fruits[1:3] = ["apple", "piyara", "waterMelon"]
print("change fruits[1:3] : ", fruits)
fruits.insert(2, "akh")
print("insert : ", fruits)
fruits.append("kul")
print("append : ", fruits)
name.extend(numbers)
print("extend between name & numbers : ", name)
fruits.remove('kul')
print('remove : ',fruits)
# fruits.clear()
# print(fruits)
######### loop ########
print('--------loop------')
for x in fruits:
    print(x)
print('-----using len-----')
for x in range(len(fruits)):
    print(fruits[x])
print('------while loop-------')
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
print('-----using print-----')
[print(x) for x in fruits]

print('-------comprehensive-------')
newFruits=[]
for x in fruits:
    if 'a' in x:
        newFruits.append(x)
print(newFruits)
print('------sort list-----')
numbers.sort()
print('sort : ',numbers)
numbers.reverse()
print('reverse : ',numbers)
numbers.sort(reverse=True)
print('reverse : ',numbers)
