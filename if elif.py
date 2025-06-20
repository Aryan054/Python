# write a program to check whether the enter character upper case ,lower case , digit or sppecial character

char = input(" character: ")
if char.isupper():
    print("it is upper")
elif char.islower():
    print("it is lower")
elif char.isdigit():
    print("it is digit")
else:
    print("special character")


#write a program to check whether integer is single digit ,double digit ,triple digit or more than 3 digit


ln = int(input("enter integer: "))
n = str(ln)
if len(n) == 1:
    print("single digit")
elif len(n) == 2:
    print("double digit")
elif len(n) == 3:
    print("triple digit")
else:
    print("more than three")

# write a program to find greatest of three number 

num1 = int(input("number1: "))
num2 = int(input("number2: "))
num3 = int(input("numbre3: "))
if num1 > num2 and num1 > num3:
           print("num 1 is greater: ". num1)
elif num2 > num1 and num2 > num3:
    print("num2 is greater: " ,num2)
elif num3 > num1 and num3 > num2 :
    ("num3 is greater: ", num3)
else:
     print("done")

"""consider a character input ,if it is upper case print the first digit of acii value, if it is lower case print last digit of its ascii value,
if it is digit print the reminder when it is divided by 3 else print the same character """

asci = input("check character: ")
a = ord(asci)
n = str(a)
if len(n.isupper) == [0]:
    print("ascii 1st value")
elif len(n.islower) == [-1]:
    print("acii last value")
elif len(n.isdigit):
    print("reminder")



