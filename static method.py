'''class Bank:
    Bname = 'kotak mahindra'
    Branch = 'Hinjewadi Phase 1'
    IFSC = 'KMH000'
    Br_code = 9211

    def __init__(self, name, acc_no,phone,acc_ty,bal=0):
        self.name = name
        self.account = acc_no
        self.contact = phone
        self.acc_type = acc_ty
        self.balance = bal

    @classmethod
    def ch_branch(cls):
        cls.Branch = cls.get_addr()

    @staticmethod
    def get_addr():
        return input('enter new branch addr: ')

    @classmethod
    def display(cls):
        print(cls.Bname,cls.Branch, cls.IFSC, cls.Br_code)

    def ch_ph(self, new):
        self.contact = new

    def disp(self):
        print(self.name, self.contact, self.acc_type, self.balance)

    @staticmethod
    def sub(bal, money):
        return bal - money
    
    @staticmethod
    def add(bal, money):
        return bal + money

    def withdraw(self, new):
        self.balance =self.sub(self.balance, new)

    def deposite(self, new):
        self.balance = self.add(self.balance, new)

cust1 = Bank('Romit', 768909876543, 5648790765, 'savings', 5000)
cust2 = Bank('Toshi', 987906574323, 8765743256, 'current', 3000)

cust1.disp()
cust1.withdraw(2000)
cust1.disp()
print()
cust2.disp()
cust2.deposite(1500)
cust2.disp()

Bank.display()
Bank.ch_branch()
Bank.display()'''

    
class Qspiders:
    python_trainer1 = 'mehal mam'
    python_trainer2 = 'Tushar sir'
    branch_head = 'Abhishek Sir'

    def __init__(self, n, id):
        self.name = n
        self.id = id

    @classmethod
    def disp(cls):
        print(cls.python_trainer1, cls.python_trainer2, cls.branch_head)

    @classmethod
    def ch_trainer(cls, new):
        cls.python_trainer2 = new

stu1 = Qspiders('Sakshit', 2587)
stu1.disp()
stu1.ch_trainer('Mohith Sir')
stu1.disp()





        
