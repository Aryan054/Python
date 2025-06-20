#wap to coonvert given decimal t0 binary

'''
def binary(n):
    res = 0
    unit = 1
    while n>0:
        rem = n%2
        res += rem * unit
        unit *= 10
        n //= 2
    return res
'''
'''
def decimal(n):
    res = 0
    unit = 0
    while n>0:
        rem = n%10
        res += rem *(2**unit)
        unit +=1
        n //= 10
    return res

'''
def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def LCM(a,b):
    return (a*b)//gcd(a,b)
    
    


