class Trainer:
    subject = 'Python'

class Stu1(Trainer):
    sub1 = 'SQL'
    sub2 = 'POWER BI'
    sub3 = 'WEBTECH'
    sub4 = 'APPTITUDE'

    @classmethod
    def disp(cls):
        print(cls.sub1,cls.sub2,cls.sub3,cls.sub4,cls.subject)

class Stu2(Trainer):
    sub5 = 'testing'
    sub6 = 'comunication'

    @classmethod
    def display(cls):
        print(cls.sub5, cls.sub6, cls.subject)

obj = Trainer()
obj = Stu1()
obj.disp()
obj = Stu2()
obj.display()
