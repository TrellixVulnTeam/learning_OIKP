#정수형 변수 a,b를 관리하는 클래스를 만들어 보자. 단 캡슐화로 구현해보자.
#풀 캡슐화
# ->은닉된 멤버 변수에게 setXX으로 값 전달 및 변경하고 getXX return 메소드로 값을 리턴하는 구조

class Test:
    __a = 0 #주소 히든 private, 주로 초기값은 원래 생성자에 전달.
    __b = 0

    #name = "abc" def setName(): 헝가리 기법 - 네이밍 규칙.

    def setA(self,a): #a는 외부에서 값을 받기 위한 argument
        self.__a = a #객체 생성 후 a값을 멤버변수인 __a에 전달(update)하겠다.
    def getA(self):
        return self.__a

    def setB(self,b):
        self.__b=b
    def getB(self):
        return self.__b

if __name__ == '__main__':
    t1 = Test()
    t1.setA(100)
    print(t1.getA())
    t1.setB(200)
    print(t1.getB())

