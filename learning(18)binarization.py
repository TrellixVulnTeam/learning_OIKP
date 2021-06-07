#이진화를 시켜보자
def binary01():
    with open('binary01.txt','wb') as f:
        for i in range(5):
            f.write(b"Do you have any problem with writing things in English?9\n")

#한글 이진화
def binary02():
    with open('binary02.txt','wb') as f:
        for i in range(5):
            f.write(bytes("대한민국만세\n",'utf-8')) #바이트 넣고 utf-8넣어주는거 잊지 말기.

def binary03():
    with open('binary01.txt','rb') as f:
        for i in f:
            print(i.decode(encoding='utf-8'),end='')     #읽을 때는 디코딩

binary03()
