class A():
    def __str__(self):
        return "str method is called"
    def __repr__(self):
        return "repr method is called"

if __name__ == '__main__':
    #print function represents parameters after processing it as string.
    """
>>> class A():
...     def __str__(self):
...         return "str method is called"
...     def __repr__(self):
...         print("dd")
...         return "repr method is called"
...
>>> x = A()
>>> x
repr method is called
>>> x
repr method is called
>>> print(x)
str method is called
"""
