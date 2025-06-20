'''#create class and initialize 5 class members
class Google:
    GoogleSearch = 'searchengine'
    GoogleAds = 'advertising'
    GoogleCloud = 'storage'
    GoogleMaps = 'navigation'
    GooglePay = 'payment'
    
#initialize 4 object members     
    def __init__(self,eid, na, dept, sal):
        self.employee = eid
        self.name = na
        self.department = dept
        self.salary = sal
        
    @classmethod
    def mod(cls,SearchBar,Marketing,Cloud,Direction,MoneyTransfer):
        cls.GoogleSearch = SearchBar
        cls.GoogleAds = Marketing
        cls.GoogleCloud = Cloud
        cls.GoogleMaps = Direction
        cls.GooglePay = MoneyTransfer

    def modify(self,emp,na,dept,sal):
        self.employee = emp
        self.name = na
        self.department = dept
        self.salary = sal
    
        
    @classmethod
    def disp(cls):
        print(cls.GoogleSearch,cls.GoogleAds,cls.GoogleCloud,cls.GoogleMaps,cls.GooglePay)

    def display(self):
        print(self.employee,self.name,self.department,self.salary)
        
emp1 = Google(1234,'Priya','development',4324)
emp2 = Google(4321, 'PAri','Testing',2367)
emp3 = Google(8987,'rohit','Nanager',7689)
    
emp1.display()
emp2.display()
emp3.display()
print()


    
emp1.modify(7686,'prit','data analysis',3456)
emp2.modify(6543,'rahul','Consultant',3467)
emp3.modify(3241, 'vikrant', 'AI/ML Engineer',8765)
    
emp1.display()
emp2.display()
emp3.display()

emp1.mod('searchbar','adds','cloud','maps','pay')
emp1.disp()'''


class Qspiders:
    pythontrainer1 = 'mam'
    pythontrainer2 = 'tushr sir'
    sqltrainer = 'colin sir'
    head = 'abhishek sir'

    def __init__(self,name,mobile,degree,gender):
        self.name = name
        self.mobile = mobile
        self.degree = degree
        self.gender = gender

    @classmethod
    def mod(cls,pythontrainer1,pythontrainer2, sqltrainer, head):
        cls.pythontrainer1 = pythontrainer1
        cls.pythontrainer2 = pythontrainer2
        cls. sqltrainer = sqltrainer
        cls.head = head

    def modify(self,name,mobile,degree,gender):
        self.name=name
        self.mobile=mobile
        self.degree=degree
        self.gender=gender

    @classmethod
    def disp(cls):
        print(cls.pythontrainer1,cls.pythontrainer2,cls.sqltrainer, cls.head)

    def display(self):
        print(self.name, self.mobile, self.degree, self.gender)
        

stud1 = Qspiders('aryan', 8767514749, 'b.e', 'male')
stud2 = Qspiders('jidnesh', 7867549087, 'b.e', 'male')

print('students details: ')
stud1.display()

stud1.modify('rahul',1234567890, 'bca', 'male')
stud1.display()
print()

print('traines details: ')
stud1.disp()

stud1.mod('mam','mohith sir','collin sir', 'abhishek sir')
stud1.disp()


    
