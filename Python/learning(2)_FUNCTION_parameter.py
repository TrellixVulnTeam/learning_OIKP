#함수의 가변 인자 값 전달
#def name(paramter1, parameter2 = x, *args(tuple), **args(dict))
# *args means 순서가 있는 나열형 목록. 그것이 리스트이건 튜플이건 튜플로 처리가 된다.
# **agrs mean dict type will be declared
#일반 매개변수, 가변 매개변수가 선언될 때 가변변수는 반드시 일반 매개변수 뒤에 하나만 선언된다.


'''
#Example
def test01(a,*b): #O
    pass

def test02(a, *b,c): #X
    pass

def test03(*a,*b): #X
    pass

def test04(a,b, *c): #O
    pass

def test05(a,b=2, *c): #O
    pass
'''


def test(*args):
    print(args,type(args))

def my_fun(a,*args,**kwargs):#a는 일반, args는 튜플, kwargs는 딕셔너리
    print('a =',a)
    print('args =',args)
    print('kwargs =',kwargs)



if __name__ == '__main__':
    #test((1,2,3,4,5))
    #test([1, 2, 3, 4, 5])
    #test("1, 2, 3, 4, 5")
    #my_fun(11)  # a =11, args = () , kwargs = {}
    my_fun(11,22,33) # a=11, arge(22,33)
    #my_fun(11, 22, 33, id ='a123', pw=1234)  # a=11, arge(22,33)

