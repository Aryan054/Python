# write a program to login in application with valid username and valide password (entre the password only if username is valid)
use = "Aryan"
pa = "123"
user = input("enter username: ")
pas = input("enter password: ")

if use == user:
    print("enter pass")
    if pa == pas:
        print("login susscefully")
    else:
        print("invalid pass")
    
# write a program to print the last value of list only if it is palindrom string starting with vowel

a = eval(input("enter value: "))

if type(a) == list:
    if type(a[-1]) == str:
        if a[-1] == a[-1][::-1]:
            if a[-1][0] == ["a,e,i,o,u,A,E,I,O,U"]:
                print("string, palindrom starting with vowel")
            else:
                print("consonent")
        else:
            print("no match")

# write a program to print string only if it is staring with vowel ending with consonent it should have middle value 

