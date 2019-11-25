class Bicycle():

    def __init__(self,wheel_size=10,color='white'):#기본값
        self.wheel_size =wheel_size# __붙이면 private
        self.color = color

    def move(self,speed):
        print("자전거: 시속{}킬로미터로 전진".format(speed))

    def turn(self,direction):
        print("자전거: {} 회전".format(direction))

    def stop(self):
        print("자전거({},{}): 정지".format(self.wheel_size, self.color))

    def __str__(self) -> str:
        return "자전거({},{})".format(self.wheel_size, self.color)

class car(Bicycle):
    def stop(self):
        print("자동차({},{}): 정지".format(self.wheel_size, self.color))

