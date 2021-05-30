#lambda 만들어 보자.

def add(x,y):
    res= x+y
    return (res)

hap = lambda x,y : x+y #람다는 이렇게 써놓고 재활용하는 놈이 아님.



if __name__ == '__main__':
    n = add(5,3)
    print(n)
    print(hap(5,3))
    print((lambda x,y,z : x*y*z)(1,2,3)) #한번 쓰고 버리기, 자주쓰이는 형태.
    print((lambda x,y : x+y)(5,3))
    r = ['one', lambda x : x*x,10]
    print(r[0],r[1](2),r[2])

