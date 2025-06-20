class Gfather:
    prop1 = 'AGRICULTURAL LAND'

class Father:
    prop2 = 'HOUSE'
    prop3 = 'BIKE'

    @classmethod
    def disp(cls):
        print(cls.prop1,cls.prop2, cls.pro3)

class Mother:
    prop4 = 'Jwellery'

class Child(Father, Mother):
    prop5 = 'uni-cycle'

    @classmethod
    def display(cls):
        print(cls.prop2,cls.prop3,cls.prop3,cls.prop4,cls.prop5)

obj = Child()

obj.display()
