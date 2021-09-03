lst = ["Learning","is","so","amusing"]

#using lambda, you can pass in variable.
def argparse(x,y):
    #x = index
    #y = list
    print(y[x])
    return y[x]

def validation(function=None):
    if function ==":odd":
        for i in lst[::2]:
            print(i)
    elif function==":even":
        for i in lst[1::2]:
            print(i)
    else:
        return function()

validation(lambda: argparse(1,"This is so hard to understand"))
