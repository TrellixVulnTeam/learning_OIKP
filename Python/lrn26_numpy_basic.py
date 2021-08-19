import numpy as np

#1.the way you put sequence data into numpy array. It can be either list or tuple.
data1 = [0,1,2,3,4,5]  # only integer -> 32bit
a1 = np.array(data1)
print(a1.mean())

data2 = [0.1,5,4,12,0.5]
a2 = np.array(data2) #mixture of int and float -> 64bit
print(a2.std())

data3 = [[1,2,3],[4,5,6],[7,8,9]]
a3 = np.array(data3)
print(a3) #convert 2d array into more visual-friendly representation

#2. range
data4 = np.arange(0,10) #not number not inclusive.
data5 = np.arange(-5,-24,-2) #with a number indicating steps
data6 = np.arange(20)
print(data4,data5,data6)

#3. making matrix
data7 = np.arange(1,101).reshape(10,10) #numbers being created must have the same number as the size of matrix.
print(data7,data7.shape) #to check the shape of array

#4 Creating array that has x number of elements from start to stop
data8 = np.linspace(1,11,23) #11 inclusive
print(data8)


