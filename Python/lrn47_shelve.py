#Saving Variables with the shelve Module
#The shelve module implements persistent storage for arbitrary Python objects
#which can be pickled, using a dictionary-like API.

import shelve

#to save variables
def save():
    pets = ["dog","cat","mouse"]
    with shelve.open('../files/shelve') as shelf_file:
        shelf_file['pets'] = pets


def read():
    with shelve.open("../files/shelve") as shelf_file:
        print(shelf_file,type(shelf_file))
        print(shelf_file['pets'],type(shelf_file['pets']))
        print(shelf_file.keys()) #pass them to list so you can print them out.
        for i in shelf_file.keys():
            print(i)
        print(list(shelf_file.values()))

read()
