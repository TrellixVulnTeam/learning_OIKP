class student:
    def __init__(self,name,m,k,s):
        self.name =name
        self.math = m
        self.korean = k
        self.science = s

    def getSum(self):
        return self.math +self.korean+self.science
    def __eq__(self, value):
        if isinstance(value,int):
            return self.getSum() == value
        else:
            return self.getSum() == value.getSum()

    def __ne__(self, value):
        if isinstance(value,int):
            return self.getSum() != value
        else:
            return self.getSum() != value.getSum()
    def __gt__(self, value):
        if isinstance(value,int):
            return self.getSum() > value
        else:
            return self.getSum() > value.getSum()
    def __ge__(self, value):
        if isinstance(value,int):
            return self.getSum() >= value
        else:
            return self.getSum() >= value.getSum()
    def __lt__(self, value):
        if isinstance(value,int):
            return self.getSum() < value
        else:
            return self.getSum() < value.getSum()
    def __le__(self, value):
        if isinstance(value,int):
            return self.getSum() <= value
        else:
            return self.getSum() <= value.getSum()

if __name__ == '__main__':
    a = student("Min",90,30,50)
    b = student("Mi",80,80,30)
    print(a<b)
    print(b<a)
    print(b>300)
    print(b<200)
