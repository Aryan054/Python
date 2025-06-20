a = int(input("enter number: "))
if a%2==0:
    print("Even")
    
# write a program to cheak if the string is palindrome

st = input("enter value: ")
if st == st[::-1]:
    print("string is palindrome")

# write a program to cheak if the number is palindrome

num = int(input("enter Number: "))
if num  == str(num)[::-1]:
    print("it is palindrome")
    
#number is palindrome or not

num = int(input("enter num: "))
if num == str(num) [::-1]:
    print("num palindrome")

#write program to chek if the sum of two number is greater than 100

a = int(input("enter a value: "))
b = int(input("enter a value: "))
sum = a+b
if sum >100:
    print("it is greater ")

# write program to check 1-st character and last character are same

char = input(" character: ")
if char[0] == char[-1]:
        print("charater is same" )

# write a program to check a product of two number is even

a = 5
b = 7
if a*b%2==0:
        print( "product is Even")

# write a program to check all the element in list are unique

uq = eval(input("Enter a list: "))
if str(uq) != str(uq):
    print("list is unique")
 
 # consider a list input , print the value at even index if the length of list is even else print the value odd index if the length is odd

l = eval(input("list  value: "))
if len(l)%2==0:
         print(l[::2])
else:
    print(l[1::2])
        
