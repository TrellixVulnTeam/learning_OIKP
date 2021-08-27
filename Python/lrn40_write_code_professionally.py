def run_this(name:str,age:int) -> None:
    #specifying types of parameter and return is a good practice for readability

    print("My name is ",name, "I'm ",age, "years old and these are my goods: ")
    my_goods = ["apple","blueberries","cake"]
    #snake case has been recognized as a standard.

    for item in my_goods:
        print(item)
    return

if __name__ == '__main__':
    my_name = "Catalina"
    my_name.replace(my_name[0],"K")
    run_this(my_name,19)