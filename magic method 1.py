class Operator():
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a
    def __sub__(self, other):
        return self.a - other.a
    def __mul__(self, other):
        return self.a * other.a
    def __truediv__(self, other):
        return self.a / other.a
    def __floordiv__(self, other):
        return self.a // other.a
    def __mod__(self, other):
        return self.a % other.a
    def __pow__(self,n):
        return self.a ** n
    def __and__(self, other):
        return self.a & other.a
    def __or__(self, other):
        return self.a | other.a
    def __invert__(self):
        return -(self.a + 1)
    def __lshift__(self, n):
        return self.a << n
    def __rshift__(self, n):
        return self.a >> n
    def __xor__(self, other):
        return self.a ^ other.a
        
obj1 = Operator(8)
obj2 = Operator(4)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)
print(obj1 // obj2)
print(obj1 ** 3)
print(obj1 % obj2)
print(obj1 & obj2)
print(obj1 | obj2)
print(~obj1)
print(obj1 ^ obj2)
print(obj1 << 2)
print(obj1 >> 2)
