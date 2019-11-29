class Bicycle():
    def __init__(self,wheel_size=20,color="black"):
        self.wheel_size =wheel_size
        self.color=color

    def move(self,speed=0):
        print("자전거 : 시속{} 킬로미터로 전진".format(speed))

    def turn(self,direction):
        print("자전거:{}회전".format(direction))

    def stop(self):
        # print("자전거({},{}): 정지".format(self.wheel_size,self.color))
        pass
    def __str__(self) -> str:
        return "자전거 wheel_size:{} color:{}".format(self.wheel_size,self.color)



class FoldingBicycle(Bicycle):

    def __init__(self,state,wheel_size=20,color="black"):
        Bicycle.__init__(self,wheel_size,color)
        self.state =state

    def __str__(self) -> str:
        return "{},{}".format(super().__str__(),self.state)

    def fold(self):
        self.state ='folding'
        print("자전거: 접기, state = {}".format(self.state))

    def unfold(self):
        self.state='unfolding'
        print("자전거: 펴기, state = {}".format(self.state))

    def move(self,speed=0):
        print("접는 자전거 : 시속{} 킬로미터로 전진".format(speed))

    def stop(self):
        print("접는 자전거 : 시속{} 킬로미터로 정지                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ".format(0))

