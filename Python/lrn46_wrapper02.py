def wrapper(func):
    def inner(*args,**kwargs):
        #validation OR commands that may not pertain to will-be-wrapped function.
        if len(args) > 2:
            raise ValueError
        if isinstance(args[0],str):
            if args[0] ==":odd":
                return args[1][::2]
            else:
                return args[1][1::2]
        else:
            #execution of the will-be-wrapped function.
            print("The wrapped func started")
            result = func(*args,**kwargs)
            print("The wrapped func finished")
            return result*5
    return inner

@wrapper
def hap(x,y):
    return x+y

