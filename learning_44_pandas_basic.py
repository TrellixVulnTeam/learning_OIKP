import pandas as pd
#1 Series: with Series, you can impart index to values of 1 dimensional array.
sr = pd.Series([17000,20000,6000,3000],index=["치킨","피자","짜장면","소주"])

print(sr.values,sr.index,sr.std())

#2 DataFrame: passing 2D lists as parameter, they have row index and column index.
framevalues = [[5,4,3],[1,2,3],[3,2,4]]
row_index = ['First_row',"Second_row","Third_row"]
columns_index = ["A","B","C"]
df = pd.DataFrame(framevalues,index=row_index,columns=columns_index)
print(df)
