import pandas as pd
import requests
import json
from collections import defaultdict
import datetime
import extraction

#"transform" is not so much intuitive.
#instead, validation stage sounds just better considering what we do in this stage.

def check_if_valid(df:pd.DataFrame)->bool:

    #1 check if input data is empty
    if df.empty:
        print("No information available. Finishing execution")
        return False

    #2 Primary key check.
    #among the columns, the strongest candidates for primary key is time.
    if pd.Series(df['time']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violoated")

    #3 null check.
    if df.isnull().values.any():
        raise Exception("null has been inserted")



    #Primary key check
    #4 check that all timestaps are of period we're interested in, in this example, yesterday
    existing_data = pd.read_csv("air_pollution.csv")['time'].tolist()
    timestamps = df['time'].tolist()


    for timestamp in timestamps:
        #binary search
        if binary_search(existing_data,len(existing_data),timestamp):
            pass
        else:
            raise Exception(f"Primary key constrain has been violoated.")



#A = Array
#n = length
#T = target
def binary_search(A, n, T) :
    L = 0
    R = n - 1
    while L <= R :
        m = int((L + R) / 2)
        if A[m] < T :
            L = m + 1
        elif A[m] > T :
            R = m - 1
        else:
            return False
    else:
        return True




if __name__ == '__main__':
    #check_if_valid(extraction.weather_extract())
    df = pd.read_csv("air_pollution.csv")
    check_if_valid(extraction.weather_extract(1))