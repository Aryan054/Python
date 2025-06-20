class Bank:
    def __init__(self,name,phone,aadhar,addr):
        self.name = name
        self.phone = phone
        self.aadhar = aadhar
        self.addr = addr

    def disp1(self):
        print(self.name,self.phone,self.aadhar,self.addr)

class Up_Bank(Bank):
    def __init__(self,name,phone,aadhar,addr,pan):
        super().__init__(name,phone,aadhar,addr)
        self.pan = pan
        
    def disp2(self):
        super().disp1()
        print(self.pan)

class Up_Bank_pro(Up_Bank):
    def __init__(self,name,phone,aadhar,addr,pan,kyc):
        super().__init__(name,phone,aadhar,addr,pan)
        self.kyc = kyc
        
    def disp3(self):
        super().disp2()
        print(self.kyc)
obj1 = Up_Bank_pro('mohit',98765432,9876543,'wakad','fgh8765hj','verified')
obj1.disp3()
        
