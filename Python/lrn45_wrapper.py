
def wrapper(func):
    def inner(*args,**kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError
        print("func start")
        result = func(*args,**kwargs)
        print("func end")
        return result *100
    return inner
# A(B(3,4))

@wrapper
def sum(x,y):
    return x+y


print(sum(10,50))