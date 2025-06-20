# classify an angle based on the degree
a = int(input("Enter angle"))
if a>90:
    print("Right Angle")
elif a>90 and a<180:
    print("Obtuse angle")
elif a>0 and a<90:
    print("Acute angle")
elif a>180 and a<360:
    print("reflex angle")
elif a == 360:
    print("Compelete angle")
else:
    print("Zero Angle")
