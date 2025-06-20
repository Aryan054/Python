class Sample:
    def __init__(self,n):
        self.n = n
    def __add__(self,self1):
        return self.n + self1.n
    def __sub__(self,self1):
        return self.n - self1.n
    def __mul__(self,self1):
        return self.n * self1.n
    def __truediv__(self,self1):
        return self.n / self1.n
    def _floordiv__(self,self1):
        return self.n // self1.n
    def __mod__(self,self1):
        return self.n % self1.n
    def __pow__(self,a):
        return self.n ** a
    def __and__(self,self1):
        return self.n & self1.n
    def __or__(self,self1):
        return self.n | self1.n
    def __invert__ (self):
        return -(self.n + 1)
    def __xor__(self,self1):
        return self.n ^ self.n
    def __lshift__(self,a):
        return self.n << a
    def __rshift__(self,a):
        return self.n >> a

obj1 = Sample(8)
obj2 = Sample(2)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)

    
        
