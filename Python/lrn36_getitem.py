class Array:
    def __init__(self):
        self.arr = [1,2,3,4,5,6,7,8]
        self.dic = {'a':123,"b":53453}


    def __getitem__(self,key):
        if isinstance(key,int):
            return self.arr[key]
        if isinstance(key,str):
            return self.dic[key]


if __name__ == '__main__':

    a = Array()

    #likewise, we can access data through key : value
    print(a[1])
    print(a['a'])

