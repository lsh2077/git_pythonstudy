from chapter_08.class_def import Car

if __name__ =="__main__":
    myCar = Car()
    myCar2 = Car(size=20,color="red")
    myCar3 = Car(size=20)

    car_list=[myCar,myCar2,myCar3]
    print("자동차 총생산 대수 :{}".format((Car.isinstance_count)))
    [print(car) for car in car_list]

    Car.isinstance_count=Car.isinstance_count+1
    myCar4=Car()
    myCar.set_speed(100)
    myCar.auto_cruse()

    myCar2.set_speed(200)
    myCar2.auto_cruse()

    Car.check_type(20)
    Car.check_type(15)

    Car.count_instance()