# whrite a program to check the given list is empty or not
list = eval(input("list"))
if len(list)==0:
    print("list is empty")
else :
    print("list is not empty")

#write program to check sum of first and last digit of given number is even

num = int(input("enter 1st value: "))
n = str(num)
if (int(n[0]) + int(n[-1]))%2 == 0:
        print("it is even")
else:
    print("it is odd")

# write a program to check it is the diffence between 2 numbers is multiple of 7

a = int(input("enter a number: "))
b = int (input("enter a number: "))

if (a-b)% 7 == 0 :
    print("True")
else:
    ("False")

# write a program to check wheter a given string is having middle character not not

s = input("enter character: ")
if len(s)%2!=0:
     print("yes ")
else :
    print("no")
    
# write a program to check if two strings are of equal length but characters not same

sr1 = input("string 1: "),
sr2 = input("string 2: ")
if len(sr1) == len(sr2) and sr1 != sr2:
     print("equal length but character not same")
else:
    print("character same")
