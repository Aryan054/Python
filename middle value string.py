lt = eval(input("Enter list: "))
if len(lt)% 2 == 1:
    l = len(lt)// 2
    if type(lt[l]) ==str:
        print("having a middle value string")
    else:
        print("middle value but not string")
else:
    print("does not have middle value")
    
"""write a program too print 1st value of tupple only it is string
havinng length more than 5 and string should be palindrom"""

a = eval(input("enter value: "))

if type(a) == tuple and type(a[0]) == str:
    print("It is string")

    if len(a[0])>5 and a[0] == a[0][::-1]:
        print("it is palindrome")
    else:
        print("not palindrom")
else:
    print("length is less than 5")
      
