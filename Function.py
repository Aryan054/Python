# factorial
'''
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
for i in range(2, 31):
    print(fact(i))
'''
# WAP to return only prime no in the given list

def prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

l=['hi',10,2.3,7,[10,20],11,'hello',23,29]
for i in l:
    if type(i) == int:
        if(prime(i)):
            print(i)
    

def prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

l=['hi',10,2.3,7,[10,20],11,'hello',23,29]

if type(i)in(list,tuple,set):
    for j in i:
        print(prime(j))
      
            
            
