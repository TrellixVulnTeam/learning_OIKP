import pickle
#피클링은 객체저장을 그대로 하기위해서.
#객체는? 파이썬에서의 객체란, 모든 것
#이진화시킨다.
#이진화 푼다.

def pickle01():
    with open('pickle01.txt','wb') as f:
        a = [1, 2, 3, 4, 5]
        b = {1: a, 2: '김나영'}
        c = pickle.dumps(a)  # 이진화시킨다.
        d = pickle.loads(c)
        e = (a,b,d,c)
        for i in e:
            pickle.dump(i,f)
def pickle02():
    with open('pickle01.txt','rb') as f:
        lst = []
        while 1:
            try:
                res = pickle.load(f)
                lst.append(res)
            except:
                break
        for i in lst:
            print(i)
            if type(i) == bytes:
                i = pickle.loads(i)
                print(i)

pickle02()


