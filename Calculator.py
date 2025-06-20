def cali():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
def get():
    a = int(input('a: '))
    b = int(input('b: '))
    return a,b
print('welcome to calculator by python..')

while True:
    print('''
1. enter 1 for addition
2. enter 2 for subtraction
3. enter 3 for multiplication
4. enter 4 for division
5. enter 0 to exit from calculator''')

    n = int(input('enter your choice '))
    if n ==1:
        a,b = get()
        add(a,b)
        
    elif n ==2:
        a,b = get()
        print(sub(a,b))

    elif n ==3:
        a,b = get()
        print(mul(a,b))
    
    elif n ==4:
        a,b = get()
        print(div(a,b))

    elif n ==0:
        break

    else:
        print('Envalid choce')
calci()
        
