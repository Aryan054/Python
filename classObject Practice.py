class Mobile:
    model = 'Vivo'
    model_no = 1
    price = 20000


    def __init__(self, color):
        self.color = color
        

obj = Mobile(input('enter a color: '))
print(obj.model, obj.model_no, obj.price, obj.color)



class Mobile:
    def __init__(self, model_no, name, price, color=''):
        self.model_no = model_no
        self.name = name
        self.price = price
        self.color = color

    def display(self):
        color = ['Black', 'Blue', 'Red']
        for i in color:
            print(self.model_no, self.name, self.price, i)

obj1 = Mobile(1, 'vivo', 20000, 'red')
obj2 = Mobile(2, 'samsung', 18000, 'black')
obj3 = Mobile(3, 'iphone', 150000, 'Blue')

obj1.display()
print()
obj2.display()
print()
obj3.display()
print()

st = 'String'
st = lambda s: s if s == s[::-1] print('palindrome')else: print('not palindrome')
print(st)

 







        

        




    
    
