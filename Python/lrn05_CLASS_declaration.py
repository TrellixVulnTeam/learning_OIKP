#이름, 주소, 전화번호를 관리하는 Address라는 클래스를 선언해서 변수로 값을 저장해 보자.
#정적 변수, static 변수
# 클래스.variable_name 으로 호출한다.
class Address:
    name = "Dominica"
    addr = "seoul"
    tel = "02-0000-0000"
    def prn(self):
        print("::".join([self.name, self.addr, self.tel]))


if __name__ == '__main__':
    print(": :".join([Address.name, Address.addr, Address.tel])) #클라스의 속성(attributes)을 그대로 가져온 것
    Address.name = "Migo"
    print(": :".join([Address.name, Address.addr, Address.tel]))

    a1 = Address() # 클래스를 통해 객채를 생성하고 a1자체가 self가 된다.
    a1.prn()
    a1.name = "Alex"
    a1.prn()
