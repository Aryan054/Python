class Father:
    def __int__(self,name,age,live):
        self.money = name
        self.bike = age
        self.family = live
         
    @classmethod
    def disp1(cls):
        print(cls.money,cls.bike,cls.family)

class Mother:
    def __init__(self,love,kindness,look):
        self.love = love
        self.age = kindness
        self.living = look

    @classmethod
    def disp2(cls):
        print(cls.name,cls.age,cls.living)

class Child(Father,Mother):
    pass

obj = Child()
obj.dis1()
obj.disp2()
