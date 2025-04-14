class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 10:
            num=self.a
            self.a+=1
            return num
        else:
            raise StopIteration
            
    def string_iter(self,text):
        for char in text:
            yield char

nums = MyNumbers()
print('number iterator : ')
for x in nums:
    print(x)

print('\nstring iterator : ')
str_iter = nums.string_iter('arif')
for ch in str_iter:
    print(ch)