'''st = input("enter string: ")
rev = ' '
for i in st:
    rev = i + rev
print(rev)

for i in range(1,10):
    print(i)
'''
'''
# write a program to find the sum of all the floating values present in a dictionary ony if its key is of string datatype having length more than 3

data = {'three':3.2,'h':3.9,'four':4.2,1:92}
total_sum = 0.0
for key, value in data.items():
    if isinstance(key,str) and len(key) >3 and isinstance(value, float):
        total_sum += value
print("sum of float value",total_sum)
         
'''
    
# wirite a program to find the sum of all the even integer present at even index in given list
'''
a = eval(input("enter a list: "))
su = 0
for i in a[::2]:
    if i % 2 == 0 and type(i) == int:
        su +=1
print(su)
      ''' 
# write a program to print all the even numbers which are multiple of 4 and palindrome in between range of 1 to n
'''
num = int(input("enter a number: "))

for i in range(1,num+1):
    if i % 2 == 0 :
        if i % 4 == 0 and str(i) == str(i)[::-1]:
            print(i)
        
'''
# Write a program to find sum of n natural number only if it is odd
'''
a = int(input("enter number: "))
su = 0
for i in range(1,a+1):
    if i % 2!== 0:
        su += 1
    else:
        i%2!= 0
        su += 1
print(su)
'''
# WRITE a program to extract all the special charater from given string
'''
a = input("enter char: ")
for i in a:
    if not ('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
        print(i)
'''
# write a program to print a largest number in a list
'''
li = eval(input("enter list : "))
large = li[0]
for i in li:
    if i > large:
        large = i
print(large)
'''
 # write program to extract all the lower case from string only if ascii value is even
'''
a = input("enter Char: ")
for i in a:
    if 'a'<=i<='z':
        if ord(i) % 2 == 0:
            print(i)
'''
# write a program to find the sum of digit of a number
'''
a = int(input("enter num: "))
su = 0
for i in a:
    if :
        su += 1
        print(i)
'''
# write a program to count number of upper case and lower case character in string

a = input("enter Char: ")
up = 0
lc = 0
for i in a:
    if 'A'<=i<='Z':
        up +=1
    elif 'a'<=i<='z':
            lc +=1
print(up)
print(lc)


# write a program to find the average of number 5 to 10

num = int(input("enter num: "))
su = 0
for i in range (1,num):
    su += i
print(su/num)
