class Employee:
    def __init__(self, name, wage):
        self.name = name
        self.wage=wage
        self.comNumber=0
        self.comPay=0
        self.commission=False 
        self.bonus=False       

    def setCommission(self,comNumber,pay):
        self.commission=True
        self.comNumber=comNumber
        self.comPay=pay
    
    def setBonus(self,bonusPay):
        self.bonus=True
        self.comPay=bonusPay

    def comString (self,str):
        if self.commission:
            str+=" and receives a commission for {} contract(s) at {}/contract".format(self.comNumber,self.comPay)
            return(str) 
        elif self.bonus:
            str+=" and receives a bonus commission of {}".format(self.comPay)
        return(str)
    
    def get_pay(self):
        pay=self.wage
        if self.bonus:
            pay+=self.comPay
        if self.commission:
            pay+=self.comNumber*self.comPay
        return pay

    def __str__(self):
        str=self.name
        return str
    
class hourlyEmployee (Employee):
    def __init__(self, name,noHours,wagePerHours):
        super().__init__(name,wagePerHours*noHours)
        self.wagePerHour=wagePerHours
        self.noHours=noHours

    def __str__(self):
        str=super().__str__()
        str+=" works on a contract of {} hours at {}/hour".format(self.noHours,self.wagePerHour)
        str=super().comString(str)
        str+=". Their total pay is {}.".format(super().get_pay())
        return str

class monthlyEmployee(Employee):
    def __init__(self, name,wage):
        super().__init__(name,wage)
    
    def __str__(self):
        str=super().__str__()
        str+=" works on a monthly salary of {}".format(self.wage)
        str=super().comString(str)
        str+=". Their total pay is {}.".format(super().get_pay())
        return str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = monthlyEmployee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = hourlyEmployee('Charlie',100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = monthlyEmployee('Renee',3000)
renee.setCommission(4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan =  hourlyEmployee('Jan',150,25)
jan.setCommission(3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = monthlyEmployee('Robbie',2000)
robbie.setBonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = hourlyEmployee('Ariel',120,30)
ariel.setBonus(600)
