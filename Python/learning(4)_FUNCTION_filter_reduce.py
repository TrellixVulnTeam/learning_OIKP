#파이썬의 고차함수(함수를 인자로 받는 함수- high order function, 다른 함수의 결과값으로 반환하게 해주는 함수.)

#filter(function or None, iterable) ---> filter object

from functools import reduce
# import functools   and functools.reduce 도 가능


def even(x):
    return x%2==0  #boolean



def filtertest():
    print(list(filter(lambda x:x%2 ==0, range(10))))


def reduce_test():
    print(reduce(lambda x, y: x + y, range(11)))



if __name__ == '__main__':
    lis = range(10)
    print(list(filter(even,lis)))
    filtertest()
    reduce_test()
    


