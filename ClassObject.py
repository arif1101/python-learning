# the _init_() function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person('Arif', 26)
p2 = Person('Zakiya', 23)
print(p1.name,p1.age)
print(p2.name,p2.age)

# __str__() function
print('------ __str()__ -----')
print(p1)
print(p2)

# class about car 
print('--------CAR------')
class Info: 
    def __init__(carInfo, name, brand):
        carInfo.name=name
        carInfo.brand=brand
    
    def user(userInfo,userName,userAge):
        userInfo.userName=userName
        userInfo.userAge = userAge

    def printUser(userInfo):
        print('this is user info : '+ userInfo.userName,"--",userInfo.userAge)


    def myCar(carInfo):
        print('hello my car name is '+ carInfo.name);

c1 = Info('BMW','zr-sports')
c1.myCar()
c1.user('arif',26)
c1.printUser()
        
