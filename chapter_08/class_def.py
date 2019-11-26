from typing import Type


class Car():
    isinstance_count= 0 #class변수

    def __init__(self,size=10,color='black'):
        self.size =size; #인스턴스 변수
        self.color =color;
        Car.isinstance_count = Car.isinstance_count+1
        Car.count_instance()

    def __str__(self) -> str:
        return "color {} size {}".format(self.size,self.color)

    def set_speed(self, speed):
        self.speed=speed

    def auto_cruse(self):#인스턴스메서드
        print("자율주행모드")
        print("{} 속도로 자율주행".format(self.speed))

    @classmethod
    def count_instance(cls):
        print("자동차 생산대수: %d" % (Car.isinstance_count))

    @staticmethod
    def check_type(model_code):
        if model_code >= 20:
            print("이 자동차는 전기차")
        elif 10<=model_code<20:
            print("이 자동차는 가솔린")
        else:
            print("똥차")