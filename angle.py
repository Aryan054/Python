#write a program to print middle value of list only if it is string
a = eval(input("Enter a list"))
if type(len(a)/2):
    if a == str:
        print("it is middle value")
    else:
        print("Not a string")
else:
    print("no middle value")
    
