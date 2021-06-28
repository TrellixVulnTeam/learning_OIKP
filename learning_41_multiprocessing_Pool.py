import time
import multiprocessing

def multi(x):
    time.sleep(2)
    return x*x


if __name__ == '__main__':
    with multiprocessing.Pool(10) as p:
        #put a sequence of data as parater of map in order
        a = p.map(multi,range(10))
        print(a)

        #the following map will return things not in order
        for i in p.imap_unordered(multi,range(10)):
            print(i)

print("finished time : " , time.perf_counter())