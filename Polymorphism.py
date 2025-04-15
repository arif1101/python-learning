class cat:
    def sound(self):
        return 'meow'
class dog:
    def sound(self):
        return 'Woof'

# function that use polymorphism
def animal_sound(animal):
    print(animal.sound())

c = cat()
d = dog()
animal_sound(c)
animal_sound(d)

# real life example 
print('-------real life example-------')
class Document:
    def show(self):
        print("Displaying document content");
class PDF(Document):
    def show(self):
        print("Showing PDF content");
class Word(Document):
    def show(self):
        print('Opening Word document')
def display(doc):
    doc.show()

display(PDF())
display(Word())

# 🔑 Key Benefits of Polymorphism:
# Cleaner and more readable code

# Flexible and extensible

# Makes your code easier to maintain
