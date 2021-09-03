from dataclasses import dataclass, asdict
"""
Dataclasses are python classes but are suited for storing data objects. 
This module provides a decorator and functions for automatically 
adding generated special methods such as __init__() and __repr__() to user-defined classes.
"""

from typing import Any

@dataclass
class Number:
    val:int

    # If you don't want specify the datatype then, use :: typing.Any
    address :Any

    #It is easy to add default values to
    #the fields of your data class.
    count : int=0
    price : float=0.0



if __name__ == '__main__':
    obj = Number(val=2,address="shit")
    print(obj.address)
    print(asdict(obj))
    import itertools

    shapes = ['circle', 'triangle', 'square', 'pentagon']
    selections = [True, False, True, False]
    for i in itertools.compress(shapes,selections):
        print(i)