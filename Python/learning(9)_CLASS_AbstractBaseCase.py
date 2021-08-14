from abc import abstractmethod, ABCMeta


class ppcom(metaclass=ABCMeta):
    def __init__(self,n,a):
        self.name = n
        self.age = a
    @abstractmethod
    def inc(self): #incentive
        pass
    @abstractmethod
    def tt_inc(self): #total income
        pass
    @abstractmethod
    def sf_degree(self): #satisfaction_degree
        pass

class planning(ppcom):
    __bspay = 250
    def __init__(self,n,a,b=300, incentive = True,tb = 'good'):
        super().__init__(n,a)
        self.incentive = incentive
        self.__teambonding = tb
        self.__bspay = b

    @property  # you don't have to put object_name.getBpay'()', just object_name,getBpay
    def Bpay(self):
        return self.__bspay
    @Bpay.setter   # objectname.Bpay = 300
    def Bpay(self, b):
        self.__bspay = b


    def inc(self):
        if (self.incentive):
            return self.__bspay*(0.3)
        else:
            return 0
    def tt_inc(self):
        return self.__bspay + self.inc()

    def sf_degree(self):
        if self.incentive == True and self.__teambonding == 'good': # why possible to access?
            return 10
        elif self.incentive == True or self.__teambonding == 'good':
            return 7
        else:
            return 3
    def emp_inf(self):
        print('*Employment statement*')
        lst2 = [self.name,self.age,self.__bspay,self.incentive,self.tt_inc(),self.sf_degree()]
        lst1 = ['Name','Age','Basic income','Incentive','Total Income', 'Satisfaction rate']
        for i,j in zip(lst1,lst2):
            print(i.ljust(18),str(j).ljust(5),sep=': ')
if __name__ == '__main__':


    p2 = planning('Alexa',32)
    p2.emp_inf()
    p2.bPay = 500
    print(p2.bPay)