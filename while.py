#wirite progam to print 1 to 10
'''
i =1
while i<=10:
     print(i)
     i +=1

# write a program to print 1 to 10 in reverse

i = 10
while i>=1:
    print(i)
    i -=1

#write a program to print n natural numbers
i = 1
num = int(input("natural numbers: "))
while i<=num:
    print(i)
    i += 1

# write a program to print all the even number from 1 to 100

i = int(input())
num = int (input("even numbers: "))
while i<= num:
    if i % 2 == 0:
        print(i)
    i += 1
'''
'''
# Write a program to print table 
i = 1
num = int(input(" enter a number : "))
while i<=10:
    print(f'{num} X  {i} = {num*i}')
    i +=1
'''
'''
# wite a program to find sum of N natural numbers

i = 1
num = int(input("sum of : "))
res = 0
while i<=num:
    res = res+i
    i +=1
print(res)

# write a program to find factorial of N natural number


num = int(input("enter a factorial: "))
i = 1
res = 1

while i<= num:
    res = res * 1
    i += 1
    
print(res)
'''

# write a program to find all a string values present in a list

'''
lt= eval(input(" enter list: "))

ex = []
i = 0
while i <= len(lt):
    if type(lt[i]) == str:
        ex.append(lt[i])
    i +=1
print(ex)
'''
# write a program to reverse a given integer without using a typecasting and slicing
'''
ln = int(input(" inter integer: "))
i = 0
while i < len(ln):
     num = len(ln).reverse()
     i +=1
print(num)

'''
'''
num = 123
res = 0
while num !=0:
    ld = num % 10
    res = res * 10 + ld
    num = num // 10
print(res)
'''
# # wirte a program to following output input is hey how are you output is hey_how_are_you
'''
ip = "hey how are you"
op = " "
i = 0
while i < len(ip):
    if ip[i] == " ":
        op = op + "_"
    else:
        op = op + ip[i]
    i += 1
print(op)
       
    '''
# write a program to extract all the special chacter from the string
'''
ip = input("enter char: ")
i = 0
op = []
while i < len(ip):
    if 'A'<= ip[i] <='z':
        pass
    if 'a'<= ip[i] <='z':
        pass
    if '0' <= ip[i] <= '9':
        pass
    else:
        op.append(ip[i])
    '''
# write a program the following output
# inp = "abcd'
# o/p = {'a':23, 'b': 34, 'c': 87, 'd': 54}
'''
a = "abcd"
i = 0
op = {}
while i < len(a):
      op[a[i]] = ord(a[i])
      i += 1
print(op)
'''
# write a program to get following output
# in = ["hello','bye', 'bajaj']
# op = ["hello":'he', "bye":'be', "bajaj":'bj']
'''
inp = ['hello','bye', 'bajaj']
out = []
i = 0
while i < len(inp):
    if type(inp[i] == str:
        out[inp[i] = inp[i][0] + inp[i][-1]]
    i +=1
print
'''

# write a program to get following output
# inp = 'HeLlo'
# op = ''hElLO'
'''
inp = 'HeLlo'
op = ' '
i = 0
while i < len(inp):
    if 'A'<= inp[i] <='Z':
        op += chr(ord(inp[i])+32
    elif 'a'<= inp[i] <='z':
        op += chr(ord(inp[i])-32
    else
        s += st[i]
    i +=1
print(op)
'''
# write a program to remove duplicate values from list withauot typecasting into set
'''        
lt = [1,2,3,4,5,6,7,1,5]
out = []
i = 0
while i < len(lt):
    if lt[i] not in out:
        out.append(lt[i])
    i+=1
print(out)
'''
# write a program to check the program is armstrong or not
'''
a = int(input("enter a value: "))
n1 = num
n2 = num
count = 0
res = 0
while n1 != 0:
    count +=1
    num //=0

while n1 != 0:
    ld = n1 % 10
    res = res + ld**count
    n1 //= 10
if  res == n2:
    print(f'{n2} is armstrong')
else:
    print(f'{n2} is not an armstrong number')
   if 
'''
    
# write a program to count number of occurace specified charecter(without using inbuilt function)
'''
a = input("enter char: ")
ch = input("Enter Chracter: ")
count = 0
i =0
while i < len(a):
    if a[i] == ch:
        count += 1
    i += 1
print(count)
'''
# write a program to reverse a string (without using slicing)
'''
st = input("enter char: ")
rev = " "
i = 0
while i <len(st):
    rev = st[i] + rev
    i +=1
print(rev) '''

# FIbonacci series 

n = int(input('enter number: '))
i= n
n1 = 0 
n2 = 1
print(n1, n2 )
while i > 0:
    n3 = n2 + n1
    print(n3)
    n1 = n2
    n2 = n3
    i -=1
    
    
