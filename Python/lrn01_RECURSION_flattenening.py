#recursion - memorization

dictionary= {1:1,2:1}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output


print(fibonacci(9)) # 1 1 2 3 5 8 13 21 34


#practice - flatten


# example = [[1,2,3],[4,[5,6]],7,[8,9]] -> [1,2,3,4,5,6,7,8,9]

def flatten(data):
    #base case
    lst = []
    for i in range(len(data)):
        if type(data[i]) != type(list()):
            lst.append(data[i])
    #recursive case
        else:
            lst += flatten(data[i])
    return lst #last in, first out


example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("Original:", example)
print("Flattened:", flatten(example))

