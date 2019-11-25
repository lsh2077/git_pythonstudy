from chapter_08.class_study import Bicycle, car

if __name__ == "__main__":
    my_bicycle = Bicycle()
    # my_bicycle.wheel_size=26
    # my_bicycle.color = "red"

    # my_bicycle.stop()
    # print(my_bicycle)
    #
    # my_bicycle=car()
    # my_bicycle.wheel_size= 35
    # my_bicycle.color='black'
    # my_bicycle.stop()

    my_bicycle2 = Bicycle(30,"black")
    # my_bicycle2.wheel_size =30
    # my_bicycle2.color="black"





    [print(c) for c in [my_bicycle,my_bicycle2]]
    print(my_bicycle.wheel_size)
