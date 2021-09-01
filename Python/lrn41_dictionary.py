#1 get() Method
#Get has two parameters: key and default value if the key did not exist
def get_method() -> None:
    picnic_items = {'apples': 5, 'cups': 2}
    print("I am bringing {} cups".format(str(picnic_items.get('cups',0))))
    print("I am bringing {} eggs".format(str(picnic_items.get('eggs',0))))



#2 setdefault() Method
#Consider this;
def setdefault_method() -> None:
    spam = {'name': 'Pooka', 'age': 5}
    if 'color' not in spam:
        spam['color'] = 'black'
    print(spam['color'])

    #succinct way
    spam.setdefault("address","Gangnam")
    print(spam['address'])

    #it doesn't change value that has been already set.
    spam.setdefault("address", "Gangbuk")
    print(spam['address'])


#3 Merge two dictionaries
def merge_dict() -> None:
    x = {"a":1, "b":2}
    y = {"b":3, "c":4}

    z = {**x,**y}
    print(z)

if __name__ == '__main__':
    merge_dict()