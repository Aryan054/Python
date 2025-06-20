
class Father:
    Home = 'home'
    Cycle = 'cycle'
    Vehicle = 'bike'

    @classmethod
    def Disp(cls):
        print(cls.Home,cls.Cycle, cls.Vehicle)

class Child(Father):
    name = 'Aryan'
    Living = 'flat'
    study = 'Engineering'

    @classmethod
    def display(cls):
        super().Disp()
        print(cls.name, cls.Living, cls.study)


obj1=Child()
obj1.display()
obj1.Disp()




class Father:
    prop1 = 'house'
    prop2 = 'farm'

    @classmethod
    def disp(cls):
        print(cls.prop1,cls.prop2)

class Child(Father):
    house = 'ghar'
    vehicle = 'uni-cycle'

    @classmethod
    def display(cls):
        print(cls.house,cls.vehicle)

obj1 = Child()
obj1.disp()
obj1.display()



class A:
    a = 10
    b = 20

    @classmethod
    def disp(cls):
        print(cls.a,cls.b)

class B(A):
    c = 30
    d = 40

    @classmethod
    def display(cls):
        print(cls.c, cls.d)

obj1 = B()
obj1.disp()
obj1.display()
    
