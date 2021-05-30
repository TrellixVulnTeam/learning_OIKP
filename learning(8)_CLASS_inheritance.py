#간단한 구조의 상속을 구현해 보자 기본 상속구조
#이름과 나이를 관리하는 Person 클래스가 있다.
#Student 클래스를 만들면서 Person을 상속 받아 '학년만' 추가하고 싶다.
# 름,나이, 학년을 모두 출력하는 클래스를 만들어보자

class Person:
    _b = 10 #강한 private형식은 멤버만 호출이 가능하다. 후손은 호출이 불가능. 약한 private(_)이면 가능
    def __init__(self, name, age,b): #5 선조의 객체가 이때 생성되면서 멤버변수에게 값 전달. 후손의 생성자로 리턴
        self.name = name
        self.age = age
        self._b = b
    def personInfo(self): #멤버변수 출력용 메소드
        return self.name + " : (age : " + str(self.age) +")"


class Student(Person): #2
    def __init__(self,name,age, b,grade): #3 후손의 주소는 먼저 확보
        Person.__init__(self,name,age,b) #4 선조의 생성자 여기서 self는 후손의 주소, 선조의 객체가 먼저 생성.
        # This enables 'class Students' to get parameter in a simliar way to class Person
        # otherwise you will have to write codes as follows
        #self.name = name
        #self.age = age   (...)


        self.grade = grade  #6 객체 생성하면서 grade변수 값 전달. 후손 객체 생성 완료.
    def GetStudent(self):
        print('b= ', self._b)
        return self.personInfo() + ", grade :" + str(self.grade) #

if __name__ == '__main__':
    x = Student("Ruri",7,3,5) #1   #7 생성된 선조의 주소를 리턴(후손 클라스가 참조하는).
    print(x.GetStudent())
    print(x.personInfo())


