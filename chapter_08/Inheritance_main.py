from chapter_08.Inheritance_class import Bicycle, FoldingBicycle

if __name__=="__main__":
    myBicycle =Bicycle(wheel_size=26,color="red")
    myFoldBicycle = FoldingBicycle("folding",wheel_size=30,color="blue")

    cycle_list = [myBicycle,myFoldBicycle]

    [print (bicycle) for bicycle in cycle_list]

    [cycle.stop() for cycle in  cycle_list]